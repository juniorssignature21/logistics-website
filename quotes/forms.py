from django import forms

from .models import QuoteRequest


class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = [
            "name", "email", "phone", "freight_type", "departure",
            "city_deliver", "incoterms", "weight", "dimensions", "ship_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["freight_type"].widget = forms.Select(choices=QuoteRequest.FREIGHT_CHOICES)
        self.fields["weight"].required = True
        self.fields["departure"].required = True


class QuickQuoteForm(forms.ModelForm):
    CITY_CHOICES = [
        ("", "Select City"),
        ("Denver", "Denver"),
        ("Sydney", "Sydney"),
        ("London", "London"),
        ("Karachi", "Karachi"),
        ("Lagos", "Lagos"),
    ]
    QUICK_FREIGHT_CHOICES = [
        ("", "Select Freight"),
        ("Air Freight", "Air Freight"),
        ("General Cargo", "General Cargo"),
        ("Bulk Cargo", "Bulk Cargo"),
        ("Oversized Cargo", "Oversized Cargo"),
    ]

    city_deliver = forms.ChoiceField(choices=CITY_CHOICES, label="Delivery City")
    freight_type = forms.ChoiceField(choices=QUICK_FREIGHT_CHOICES, label="Freight Type", required=False)
    weight = forms.CharField(label="Weight", required=False)

    class Meta:
        model = QuoteRequest
        fields = ["name", "email", "phone", "city_deliver", "freight_type", "weight"]

    def clean_weight(self):
        raw = (self.cleaned_data.get("weight") or "").strip()
        if not raw:
            return None
        try:
            return float(raw)
        except ValueError:
            raise forms.ValidationError("Enter weight as a number, e.g. 120.")
