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
    url(r'^aeromodelling-club', include('aero.urls')),
    url(r'^erc', include('erc.urls')),
    url(r'^biotech-club', include('biotech.urls')),
    # url(r'^krittika', include('krittika.urls')),
    url(r'^$',main.views.index),
    url(r'^alumni',main.views.alumni),
    url(r'^hall-of-fame$',main.views.hof),
    url(r'^login$',main.views.login),
    url(r'^team-2012-13$',main.views.team2012),
    url(r'^team-2013-14$',main.views.team2013),
    url(r'^team-2014-15$',main.views.team2014),
    url(r'^team-2015-16$',main.views.team2015),
    url(r'^team-2016-17$',main.views.team2016),
    url(r'^team-2017-18$',main.views.team2017),
    url(r'^tech-gcrankings-2016-17$',main.views.gcrankings),
    url(r'^srg', include('srg.urls')),
]
