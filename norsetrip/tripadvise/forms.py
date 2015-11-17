from django import forms

from .models import Lodge

class LodgeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('lodge_name', 'lodge_address',)