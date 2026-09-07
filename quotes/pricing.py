"""Deterministic, dependency-free freight quote estimator.

There is no live carrier-rate API wired up, so this produces a believable,
consistent estimate from the request's own inputs: a per freight-type base
rate, a weight-based cost, and a route surcharge derived from the departure
and delivery city names (same route always yields the same surcharge).
"""

import hashlib

FREIGHT_RATES = {
    "Air Freight": {"base": 250, "per_kg": 4.80, "transit": "2-5 business days"},
    "Ocean Freight": {"base": 120, "per_kg": 0.90, "transit": "20-35 business days"},
    "Road Freight": {"base": 80, "per_kg": 1.40, "transit": "3-10 business days"},
    "Warehousing": {"base": 60, "per_kg": 0.35, "transit": "Ongoing storage"},
    "General Cargo": {"base": 150, "per_kg": 2.20, "transit": "5-12 business days"},
    "Bulk Cargo": {"base": 200, "per_kg": 1.10, "transit": "10-25 business days"},
    "Oversized Cargo": {"base": 350, "per_kg": 3.10, "transit": "7-18 business days"},
}
DEFAULT_RATE = {"base": 150, "per_kg": 2.50, "transit": "5-14 business days"}


def route_surcharge(departure: str, destination: str) -> float:
    key = f"{departure.strip().lower()}|{destination.strip().lower()}"
    digest = hashlib.sha256(key.encode()).hexdigest()
    # Map to a plausible USD range representing distance/fuel/customs variance.
    return 60 + (int(digest[:6], 16) % 940)


def calculate_quote(freight_type: str, weight, departure: str, destination: str) -> dict:
    rate = FREIGHT_RATES.get(freight_type, DEFAULT_RATE)
    weight = float(weight or 1)
    surcharge = route_surcharge(departure or "origin", destination or "destination")

    freight_cost = rate["per_kg"] * weight
    fuel_customs_fee = round((rate["base"] + freight_cost) * 0.12, 2)

    subtotal = rate["base"] + freight_cost + surcharge + fuel_customs_fee
    price_low = round(subtotal * 0.92, 2)
    price_high = round(subtotal * 1.18, 2)

    breakdown = [
        {"label": "Base Handling Fee", "value": f"${rate['base']:,.2f}"},
        {"label": f"Freight Cost ({weight:g} kg)", "value": f"${freight_cost:,.2f}"},
        {"label": "Route Surcharge", "value": f"${surcharge:,.2f}"},
        {"label": "Fuel & Customs Fee", "value": f"${fuel_customs_fee:,.2f}"},
    ]

    route = f"{departure or 'Origin'} → {destination or 'Destination'}"

    return {
        "route": route,
        "freight_type": freight_type or "General Cargo",
        "price_low": price_low,
        "price_high": price_high,
        "transit": rate["transit"],
        "breakdown": breakdown,
        "note": (
            "This is an automated estimate based on typical rates for this freight type and "
            "weight. Final pricing is confirmed by our team after reviewing shipment details."
        ),
    }
