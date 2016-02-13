from django.conf.urls import url

from . import views

#urlresolver
urlpatterns = [
    
    url(r'^$', views.home, name ='home'),
    url(r'^courses', views.courses, name = 'courses'),
    url(r'^sample', views.sample, name = 'sample'),
    url(r'^hotels', views.hotels, name = 'hotels'),
    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/$', views.hotel_details, name ='hotel_details'),
    url(r'^post_new', views.post_new, name = 'post_new'),
    url(r'^post_course', views.post_course, name = 'post_course'),
    ]