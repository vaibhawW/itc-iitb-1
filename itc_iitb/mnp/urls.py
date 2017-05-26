from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^/about$',views.about,name='about'),
    url(r'^/blog$',views.blog,name='blog'),
    url(r'^/blog/(?P<blog_num>[0-9]+)$',views.blogNo,name='blogNo'),
    url(r'^/projects$',views.projects,name="projects"),
 	url(r'^/events$',views.events,name="events"),
       
]
