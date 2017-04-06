from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from aeroevents.models import Events

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=Events.objects.all().order_by("-happeningdate"),template_name="aeroevents/events.html")),
	
]
