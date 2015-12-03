from django import forms

from .models import Lodge

from .models import Course

class LodgeForm(forms.ModelForm):

    class Meta:
        model = Lodge
        fields = ('lodge_name', 'lodge_address', 'city', 'country', 'lodge_url', 'average_rating',)
        
class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ('name', 'dept','prof', 'term', 'year_offered',)