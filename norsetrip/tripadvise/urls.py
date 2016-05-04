from django.conf.urls import url
from django.conf.urls import include

from . import views

#urlresolver
urlpatterns = [
    
    url(r'^$', views.index, name ='index'),
    url(r'^courses', views.courses, name = 'courses'),
    url(r'^course_detail/(?P<courseId>[0-9]+)/$', views.course_detail, name = "course_detail"),
    # url(r'^sample', views.sample, name = 'sample'),
    url(r'^hotels', views.hotels, name = 'hotels'),
    url(r'^hotel_details_notuser/(?P<lodgeId>[0-9]+)/$', views.hotel_details_notuser, name ='hotel_details_notuser'),
    url(r'^food_detail_notuser/(?P<foodId>[0-9]+)/$', views.food_detail_notuser, name ='food_detail_notuser'),
    url(r'^entertainment_detail_notuser/(?P<entertainmentId>[0-9]+)/$', views.entertainment_detail_notuser, name ='entertainment_detail_notuser'),


    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/$', views.hotel_details, name ='hotel_details'),

	url(r'^hotel_details/(?P<lodgeId>[0-9]+)/edit/$',views.lodge_update, name= "lodge_update"),

    url(r'^post_lodge', views.post_lodge, name = 'post_lodge'),
    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/edit/$',views.lodge_update, name= "lodge_update"),
    
    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/editreview/$',views.review_update, name= "review_update"),
    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/deletereview/$',views.review_delete, name= "review_delete"),

    url(r'^food_detail/(?P<foodId>[0-9]+)/$', views.food_detail, name = "food_detail"),
	url(r'^food_detail/(?P<foodId>[0-9]+)/edit/$',views.food_update, name= "food_update"),
	url(r'^food_detail/(?P<foodId>[0-9]+)/editreview/$',views.foodreview_update, name= "foodreview_update"),
	url(r'^food_detail/(?P<foodId>[0-9]+)/deletereview/$',views.foodreview_delete, name= "foodreview_delete"),
	url(r'^entertainment_detail/(?P<entertainmentId>[0-9]+)/$', views.entertainment_detail, name = "entertainment_detail"),
	url(r'^entertainment_detail/(?P<entertainmentId>[0-9]+)/edit/$',views.entertainment_update, name= "entertainment_update"),
	url(r'^entertainment_detail/(?P<entertainmentId>[0-9]+)/delete/$',views.entertainment_delete, name= "entertainment_delete"),
	url(r'^entertainment_detail/(?P<entertainmentId>[0-9]+)/editreview/$',views.entertainmentreview_update, name= "entertainmentreview_update"),
	url(r'^entertainment_detail/(?P<entertainmentId>[0-9]+)/deletereview/$',views.entertainmentreview_delete, name= "entertainmentreview_delete"),



    url(r'^food_detail/(?P<foodId>[0-9]+)/delete/$', views.food_delete, name = 'food_delete'),
	#url(r'^review_detail/(?P<reviewId>[0-9]+)/$', views.review_detail, name ="review_detail"),
   

    url(r'^course_detail/(?P<courseId>[0-9]+)/edit/$',views.course_update, name= "course_update"),
    
    url(r'^post_course', views.post_course, name = 'post_course'),
    url(r'^post_food', views.post_food, name = 'post_food'),
    url(r'^post_entertainment', views.post_entertainment, name = 'post_entertainment'),

    
    

    url(r'^clAssignment', views.clAssignment, name = 'clAssignment'),

    url(r'^course/course_detail/(?P<courseId>[0-9]+)/delete/$', views.course_delete, name = 'course_delete'),

    url(r'^hotel_details/(?P<lodgeId>[0-9]+)/delete/$', views.hotel_delete, name = 'hotel_delete'),

    url(r'^post_user', views.post_user, name = 'post_user'),
    url(r'^users', views.users, name = 'users'),
    url(r'^user_detail/(?P<userId>[0-9]+)/$', views.user_detail, name = "user_detail"),
    url(r'^user_detail/(?P<courseId>[0-9]+)/edit/$',views.user_update, name= "user_update"),
    url(r'^cuAssignment', views.cuAssignment, name = 'cuAssignment'),
    url(r'^user_detail/(?P<userId>[0-9]+)/delete/$', views.user_delete, name = 'user_delete'),

    # url(r'^post_review', views.post_review, name = 'post_review'),
    url(r'add_like/$', views.add_like, name = 'add_like'),


    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}), # views.logout, name = 'logout'),
    url(r'^social-login-error', views.social_login_error, name = 'login_error'),

    
    ]
# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOTS)