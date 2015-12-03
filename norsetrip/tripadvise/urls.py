from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.home, name ='home'),
    url(r'^courses', views.courses, name = 'courses'),
    url(r'^hotels', views.hotels, name = 'hotels'),
    #url(r'^$', views.base, name ='base'),
    url(r'^post_new', views.post_new, name='post_new'),
    url(r'^post_course', views.post_course, name='post_course'),
    
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    
    ]