"""stab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from aero.models import Event

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'events$', ListView.as_view(queryset=Event.objects.all().order_by("-happeningdate"),template_name="aero/events/events.html"),name='events'),
    url(r'gallery$',views.gallery,name='gallery'),
    url(r'rcplanes$',views.rcplane,name='rcplane'),
    url(r'team$',views.team,name='team'),
    url(r'vision$', views.vision,name='vision'),
]
