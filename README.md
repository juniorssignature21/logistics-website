# Global Axis Cargo — Logistics Website (Django)

A full Django rebuild of the Global Axis Cargo logistics/transportation
website, based on the original static "TransHub" HTML template design.

## Apps

- **pages** — home, about, services, FAQ, policy, terms, sitemap; also
  holds `Service`, `FAQItem`, and the site-wide `SiteSetting` (phone,
  email, address, socials — editable from the admin).
- **contact** — contact form (`ContactMessage`).
- **quotes** — quote request form + a small server-side quote estimator
  (`QuoteRequest`), used by both the homepage quick-quote widget and the
  full `/quote/` calculator.
- **careers** — job postings and applications (`JobPosting`,
  `JobApplication`, resumes uploaded to `media/resumes/`).
- **tracking** — shipment tracking (`Shipment`, `ShipmentEvent`), looked
  up by tracking number on `/track/`.
- **stories** — the homepage "Share Your Story" testimonials
  (`Story`), moderated via `is_approved` in the admin before they show
  on the homepage.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate      # also seeds services, FAQs, jobs, demo shipments & stories
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `/admin/` to manage
content.

Demo tracking numbers seeded for `/track/`: `AWB-8F9C9B9E` (in transit)
and `AWB-3D7A1C22` (delivered).

## Configuration

Settings read from environment variables (all optional, sensible
defaults for local dev):

- `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`
- `DJANGO_EMAIL_BACKEND`, `DJANGO_EMAIL_HOST`, `DJANGO_EMAIL_PORT`,
  `DJANGO_EMAIL_HOST_USER`, `DJANGO_EMAIL_HOST_PASSWORD`,
  `DJANGO_EMAIL_USE_TLS`, `DJANGO_DEFAULT_FROM_EMAIL`,
  `DJANGO_SITE_ADMIN_EMAIL`

## Static assets

All CSS/JS/images from the original template live under `static/`,
including self-hosted copies of Font Awesome, Bootstrap Icons,
SweetAlert2, and Leaflet under `static/vendor/` and `static/webfonts/`
(no external CDN dependency at runtime).

Run `python manage.py collectstatic` before deploying.
