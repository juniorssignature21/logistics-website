import json

from django.views.generic import TemplateView

from .models import Shipment


class TrackPageView(TemplateView):
    template_name = "tracking/track.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tracking_number"] = ""
        ctx["shipment"] = None
        ctx["searched"] = False
        return ctx

    def post(self, request, *args, **kwargs):
        tracking_number = request.POST.get("tracking_number", "").strip()
        ctx = self.get_context_data(**kwargs)
        ctx["tracking_number"] = tracking_number
        ctx["searched"] = True
        if tracking_number:
            ctx["shipment"] = (
                Shipment.objects.filter(tracking_number__iexact=tracking_number)
                .prefetch_related("events")
                .first()
            )

        map_points = []
        if ctx["shipment"]:
            for event in ctx["shipment"].events.all():
                if event.latitude is not None and event.longitude is not None:
                    map_points.append(
                        {
                            "lat": event.latitude,
                            "lng": event.longitude,
                            "label": event.location or event.status,
                            "status": event.status,
                        }
                    )
        ctx["has_map_points"] = bool(map_points)
        ctx["map_points_json"] = json.dumps(map_points)
        return self.render_to_response(ctx)
