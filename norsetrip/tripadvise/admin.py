from django.contrib import admin

# Register your models here.
from .models import Lodge
from .models import Course
from .models import Course_Lodge_Assignment
from .models import CustomUser
from .models import Review
from .models import Course_User_Assignment
from .models import Food
from .models import FoodReview
from .models import Entertainment
from .models import EntertainmentReview


#admin.site.register(Lodging)
class LodgeAdmin(admin.ModelAdmin):
	#fields = ["lodge_name", "Lodge_address", "City", "Country", "Pub_date" ]
	list_display = ("lodgeId","lodge_name","country");
	list_filter = ['country']
	search_fields = ['city']
	list_per_page = 50 #pagination

admin.site.register(Lodge, LodgeAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ("courseId",'name','dept', 'term')
	list_filter = ['name']
	search_fields = ['name']
	list_per_page = 50
admin.site.register(Course, CourseAdmin)

class Course_Lodge_AssignmentAdmin(admin.ModelAdmin):
	#list_display = ("hotel_that_was_switched", 'date_switched')
	list_display = ("clAssignId","lodge_name","course_name")
	#list_filter = ['course_Id']
	#search_fields = ['course_Id']
	
admin.site.register(Course_Lodge_Assignment, Course_Lodge_AssignmentAdmin)

class CustomUserAdmin(admin.ModelAdmin):
	list_display = ('userId','fullName','email','role')
admin.site.register(CustomUser, CustomUserAdmin)

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('reviewId','likes','lodge_Id','rating', 'pub_date')#'user_Id','rating','pub_date')
admin.site.register(Review, ReviewAdmin)

class Course_User_AssignmentAdmin(admin.ModelAdmin):
	list_display = ('courseAssignId','course_Id','user_Id')
admin.site.register(Course_User_Assignment, Course_User_AssignmentAdmin)

class FoodAdmin(admin.ModelAdmin):
	list_display = ('foodId','name','address','city', 'image',)
admin.site.register(Food, FoodAdmin)

class FoodReviewAdmin(admin.ModelAdmin):
	list_display = ('reviewId','likes','food_Id','rating', 'pub_date')#'user_Id','rating','pub_date')
admin.site.register(FoodReview, FoodReviewAdmin)

class EntertainmentAdmin(admin.ModelAdmin):
	list_display = ('entertainmentId','name','address','city', 'image',)
admin.site.register(Entertainment, EntertainmentAdmin)

class EntertainmentReviewAdmin(admin.ModelAdmin):
	list_display = ('reviewId','likes','entertainment_Id','rating', 'pub_date')#'user_Id','rating','pub_date')
admin.site.register(EntertainmentReview, EntertainmentReviewAdmin)