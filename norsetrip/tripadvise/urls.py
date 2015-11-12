from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.lodge_list, name ='lodge_list'),
    
    ]