"""itc_iitb URL Configuration

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
from django.contrib import admin
from . import views
import main.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',main.views.index),
    url(r'^team-2017-18$',main.views.team),
    url(r'^login$',main.views.login),
    url(r'^srg', include('srg.urls')),
    url(r'^tech-gcrankings-2016-17$',main.views.gcrankings),
    url(r'^aeromodelling-club', include('aero.urls')),
    url(r'^erc', include('erc.urls')),
]
