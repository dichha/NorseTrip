from django import forms

from .models import Lodge

from .models import Course

from .models import Course_Lodge_Assignment


class LodgeForm(forms.ModelForm):

    class Meta:
        model = Lodge
        fields = ('lodge_name', 'lodge_address', 'city', 'country', 'lodge_url', 'average_rating',)
        
class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = [
        'courseId',
        'name', 
        'dept',
        'prof', 
        'term', 
        'year_offered',
        'course_description',
        'course_lodge_membership']
        
class Course_Lodge_AssignmentForm(forms.ModelForm):
    
     class Meta:
         model = Course_Lodge_Assignment
        
         fields = ('lodge_Id','course_Id','hotel_that_was_switched','date_switched',)