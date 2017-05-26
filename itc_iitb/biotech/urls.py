from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
 	url(r'^/events$',views.events,name='events'),
    url(r'^/blog$',views.blog,name='blog'),
    url(r'^/tutorial$',views.tutorials,name='tutorials'),
    url(r'^/contact$',views.contact,name='contacts'),
    url(r'^/blog/(?P<blog_num>[0-9]+)$',views.blogNum,name='blogs/blog'),
 	url(r'^/tutorial/(?P<tut_num>[0-9]+)$',views.tutNum,name='tutorials/tut'),
    url(r'^',views.index,name='notFound'),
]
