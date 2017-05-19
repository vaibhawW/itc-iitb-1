from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'about',views.about,name='about'),
    url(r'events',views.events,name='events'),
    url(r'team',views.team,name='team'),
    url(r'teamstruct',views.teamstruct,name='teamstruct'),
]
