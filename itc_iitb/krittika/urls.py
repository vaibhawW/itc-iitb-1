"""temp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/$',views.index),
    url(r'^/vision$',views.vision),
    url(r'^/vision/$',views.vision),
    url(r'^/events/lectures$',views.lectures),
    url(r'^/events/lectures/$',views.lectures),
    url(r'^/events/lectures/(?P<blog_num>[0-9]+)$',views.lectureOne),
    url(r'^/events/GDs$',views.GDs),
    url(r'^/events/GDs/$',views.GDs),
    url(r'^/events/GDs/(?P<blog_num>[0-9]+)$',views.gdOne),
    url(r'^/events/trips$',views.trips),
    url(r'^/events/trips/$',views.trips),
    url(r'^/events/trips/(?P<blog_num>[0-9]+)$',views.tripOne),
    url(r'^/photos$',views.photos),
    url(r'^/VR$',views.VR),
    url(r'^/about$',views.about),
    url(r'^/team$',views.team),
    url(r'^/resources$',views.resources),
    url(r'^/resources/books$',views.books),
    url(r'^/resources/building-telescope$',views.telescope),
    url(r'^/resources/celestial-mechanics$',views.celistial),
    url(r'^/resources/Basics$',views.basics),
    url(r'^/photos/$',views.photos),
    url(r'^/VR/$',views.VR),
    url(r'^/about/$',views.about),
    url(r'^/team/$',views.team),
    url(r'^/resources/$',views.resources),
    url(r'^/resources/books/$',views.books),
    url(r'^/resources/building-telescope/$',views.telescope),
    url(r'^/resources/celestial-mechanics/$',views.celistial),
    url(r'^/resources/Basics/$',views.basics),
]
