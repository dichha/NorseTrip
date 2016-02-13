from django import forms

from .models import Lodge

from .models import Course

from .models import Membership


class LodgeForm(forms.ModelForm):

    class Meta:
        model = Lodge
        fields = ('lodge_name', 'lodge_address', 'city', 'country', 'lodge_url', 'average_rating',)
        
class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ('name', 'dept','prof', 'term', 'year_offered','lodge_membership',)
        
class MembershipForm(forms.ModelForm):
    
    class Meta:
        model = Membership
        
        fields = ('lodge','course','hotel_that_was_switched','date_switched',)