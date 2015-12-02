from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.home, name ='home'),
    url(r'^courses', views.courses, name = 'courses'),
    url(r'^hotels', views.hotels, name = 'hotels'),
    #url(r'^$', views.base, name ='base'),
    
    ]