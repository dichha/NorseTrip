from django.conf.urls import url
from django.conf.urls import include

from . import views

#urlresolver
urlpatterns = [
    
    url(r'^$', views.home, name ='home'),
    url(r'^courses', views.courses, name = 'courses'),
    url(r'^course_detail/(?P<courseId>[0-9]+)/$', views.course_detail, name = "course_detail"),
    # url(r'^sample', views.sample, name = 'sample'),
    url(r'^hotels', views.hotels, name = 'hotels'),
    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/$', views.hotel_details, name ='hotel_details'),

    url(r'^post_lodge', views.post_lodge, name = 'post_lodge'),
    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/edit/$',views.lodge_update, name= "lodge_update"),

    url(r'^course_detail/(?P<courseId>[0-9]+)/edit/$',views.course_update, name= "course_update"),
    
    url(r'^post_course', views.post_course, name = 'post_course'),
    url(r'^clAssignment', views.clAssignment, name = 'clAssignment'),

    url(r'^course_detail/(?P<courseId>[0-9]+)/delete/$', views.course_delete, name = 'course_delete'),

    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/delete/$', views.hotel_delete, name = 'hotel_delete'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}) # views.logout, name = 'logout'),

    
    ]
# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOTS)