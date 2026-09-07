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

- `DATABASE_URL` — a Postgres connection string. When unset, the app
  falls back to a local `db.sqlite3` file. See **Deploying to Railway**
  below.
- `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`,
  `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DJANGO_SECURE_SSL_REDIRECT`, `DJANGO_SECURE_HSTS_SECONDS` — HTTPS
  hardening, only take effect when `DJANGO_DEBUG=False`.
- `DJANGO_DB_CONN_MAX_AGE`, `DJANGO_DB_SSL_REQUIRE` — tuning for the
  Postgres connection (defaults: 600s persistent connections, SSL
  required).
- `DJANGO_EMAIL_BACKEND`, `DJANGO_EMAIL_HOST`, `DJANGO_EMAIL_PORT`,
  `DJANGO_EMAIL_HOST_USER`, `DJANGO_EMAIL_HOST_PASSWORD`,
  `DJANGO_EMAIL_USE_TLS`, `DJANGO_DEFAULT_FROM_EMAIL`,
  `DJANGO_SITE_ADMIN_EMAIL`

## Static assets

All CSS/JS/images from the original template live under `static/`,
including self-hosted copies of Font Awesome, Bootstrap Icons,
SweetAlert2, and Leaflet under `static/vendor/` and `static/webfonts/`
(no external CDN dependency at runtime). In production, WhiteNoise
serves these directly from the Django process — no separate static
host or CDN is required.

Run `python manage.py collectstatic` before deploying (the `Procfile`
below already does this automatically on every boot).

## Deploying to Railway

The repo ships with a `Procfile` and `.python-version`, which Railway's
Nixpacks builder picks up automatically — no Dockerfile needed.

1. **Push this repo to GitHub** and create a new Railway project from it
   (or `railway up` from the CLI).

2. **Add a Postgres database.** In the Railway project, click
   **+ New → Database → PostgreSQL**. This creates a `Postgres` service
   with connection info in its **Variables** tab, including:
   - `DATABASE_URL` — private/internal URL, only reachable from other
     services *inside the same Railway project*.
   - `DATABASE_PUBLIC_URL` — public URL (via Railway's TCP proxy),
     reachable from anywhere, including outside Railway.

3. **Point the web service at the database.** On your Django service's
   **Variables** tab, add:
   ```
   DATABASE_URL = ${{Postgres.DATABASE_PUBLIC_URL}}
   ```
   Using the *public* URL (as requested) means the app reaches the
   database over Railway's public proxy rather than private networking
   — useful if the two services ever live in different
   projects/environments, or you want the same connection string to
   work from your own machine (e.g. to run `manage.py migrate` or
   `dbshell` locally against the remote DB). If you don't need that,
   `${{Postgres.DATABASE_URL}}` (private) is slightly faster and free
   of egress cost — swap it in any time, no code changes required.

4. **Set the remaining environment variables** on the web service:
   ```
   DJANGO_SECRET_KEY = <a long random string>
   DJANGO_DEBUG = False
   DJANGO_ALLOWED_HOSTS = <your-app>.up.railway.app   # or leave unset; RAILWAY_PUBLIC_DOMAIN is auto-detected
   ```
   (`RAILWAY_PUBLIC_DOMAIN` is injected by Railway automatically and is
   already added to `ALLOWED_HOSTS` / `CSRF_TRUSTED_ORIGINS` in
   `config/settings.py`, so you only need `DJANGO_ALLOWED_HOSTS` for a
   custom domain.)

5. **Deploy.** Railway builds the app, then runs the `Procfile`'s `web`
   process, which on every boot runs `migrate`, `collectstatic`, then
   starts `gunicorn`:
   ```
   web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn config.wsgi --bind 0.0.0.0:$PORT --workers 3 --log-file -
   ```

6. **Create an admin user** once it's live, via the Railway shell for
   the service (or a local shell with `DATABASE_URL` set to the public
   URL):
   ```
   python manage.py createsuperuser
   ```

### Known limitation: file uploads

Resumes, testimonial photos, etc. (`media/`) are written to the
container's local disk, which Railway wipes on every redeploy. Fine for
a demo/first deploy; for production, swap `DEFAULT_FILE_STORAGE` for
an S3-compatible bucket (e.g. via `django-storages` + Cloudflare R2 or
AWS S3) so uploads persist across deploys.
