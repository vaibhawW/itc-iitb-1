from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from aeroevents.models import Event

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=Event.objects.all().order_by("-happeningdate"),template_name="aeroevents/events.html")),
]
