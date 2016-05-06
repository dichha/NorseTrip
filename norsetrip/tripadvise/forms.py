from django import forms
from django.utils.encoding import smart_unicode

from .models import Lodge
from .models import Course
from .models import Course_Lodge_Assignment
from .models import CustomUser
from .models import Course_User_Assignment
from .models import Review
from .models import Food
from .models import FoodReview
from .models import Entertainment
from .models import EntertainmentReview

def __unicode__(self):
	return smart_unicode(self.tag)

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
        'rqmt',
        'year_offered',
        'course_description']
        #course_lodge_assignments']
        
class Course_Lodge_AssignmentForm(forms.ModelForm):
    
     class Meta:
         model = Course_Lodge_Assignment
        
         fields = [
         'lodge_name',
         'course_name']

class CustomUserForm(forms.ModelForm):
    class Meta: 
        model = CustomUser
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

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
                            'name',
                            'address',
                            'city',
                            'country',
                            'url',
                            'descrip',
                            'image',
                            ]  
        def clean_image(self):
            image = self.cleaned_data.get['image']
            if image:
                # do some validation, if it fails
                raise forms.ValidationError(u'Form error')
            return image        
         
        
               
class FoodReviewForm(forms.ModelForm):
    class Meta:
        model = FoodReview
        fields = [
            'rating',
            'comment',
            ] 
            
class EntertainmentForm(forms.ModelForm):
    class Meta:
        model = Entertainment
        fields = [
                            'name',
                            'address',
                            'city',
                            'country',
                            'url',
                            'descrip',
                            'image',
                            ]  
        def clean_image(self):
            image = self.cleaned_data.get['image']
            if image:
                # do some validation, if it fails
                raise forms.ValidationError(u'Form error')
            return image        
         
        
               
class EntertainmentReviewForm(forms.ModelForm):
    class Meta:
        model = EntertainmentReview
        fields = [
            'rating',
            'comment',
            ] 
  
        