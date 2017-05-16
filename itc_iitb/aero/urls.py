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

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^vision$', views.vision,name='vision'),
    url(r'^events$', include('aeroevents.urls')),
    url(r'^team$',views.team,name='team'),
    url(r'^rcplanes$',views.rcplane,name='rcplane'),
    url(r'^gallery$',views.gallery,name='gallery'),
    url(r'^search$',views.search,name='search'),
]
