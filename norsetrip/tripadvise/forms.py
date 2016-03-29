from django import forms

from .models import Lodge
from .models import Course
from .models import Course_Lodge_Assignment
from .models import User
from .models import Course_User_Assignment
from .models import Review


class LodgeForm(forms.ModelForm):

    class Meta:
        model = Lodge
        fields = [
        'lodge_name',
        'lodge_image', 
        'lodge_address', 
        'city', 
        'country', 
        'lodge_url', 
        'lodge_descrip',
        ]
        
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
        'course_description']
        #course_lodge_assignments']
        
class Course_Lodge_AssignmentForm(forms.ModelForm):
    
     class Meta:
         model = Course_Lodge_Assignment
        
         fields = [
         'lodge_name',
         'course_name']

class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = [
        'userId',
        'fullName',
        'email',
        'role'
        ]

class Course_User_AssignmentForm(forms.ModelForm):
    class Meta:
        model = Course_User_Assignment
        fields = [
        'user_Id',
        'course_Id'
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
        'rating',
        'comment'
        ]
        # widgets = {
        # 'comment': Textarea(attrs = {'cols': 40, 'row': 15})
        # }

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating', 'comment']
#         widgets = {
#         'comment': forms.TextInput(
#             attrs={'required': True})
#         }
        