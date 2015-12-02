from django.http import HttpResponse
from django.shortcuts import render


from .models import Lodge
from .models import Course
# Create your views here.

def home(request):
    #lodge = Lodge.objects.all()
    return render(request, 'tripadvise/home.html')

def courses(request):
	courses = Course.objects.all()
	return render(request, 'tripadvise/courses.html')
	
def hotels(request):
	hotels = Lodge.objects.all()
	return render(request, 'tripadvise/hotels.html')