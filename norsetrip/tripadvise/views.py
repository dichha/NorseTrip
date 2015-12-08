from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import View

from django.shortcuts import redirect

from django.shortcuts import redirect

from django.shortcuts import redirect


from .models import Lodge

from .models import Course

from .models import Membership

from .forms import LodgeForm

from .forms import MembershipForm

from .forms import CourseForm
# Create your views here.

def home(request):
    #lodge = Lodge.objects.all()
    return render(request, 'tripadvise/home.html')
def sample(request):
    #lodge = Lodge.objects.all()
    return render(request, 'tripadvise/sample.html')

def courses(request):
	course = Course.objects.all()
	return render(request, 'tripadvise/courses.html' , {'course': course})
	
def hotels(request):
	lodge = Lodge.objects.all()
	return render(request, 'tripadvise/hotels.html', {'lodge': lodge})
#def course_lodge_assignment(request):
 #   course_lodge = Lodge.objects.()
def hotel_details(request,lodgeId):
    lodge_info = get_object_or_404(Lodge,pk = lodgeId);
    return render(request,'tripadvise/hotel_details.html',{'lodge_info':lodge_info})
    

def post_new(request):
    if request.method == "POST":
        form = LodgeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('tripadvise.views.post_detail.html',)
    else:
        form = LodgeForm()
    return render(request, 'tripadvise/post_edit.html', {'form': form})
def membership_new(request):
    if request.method == "POST":
	form = MembershipForm(request.POST)
	if form.is_valid():
	    post = form.save(commit=False)
	    post.save()
	    
    else:
	form = MembershipForm()
    return render(request, 'tripadvise/membership.html',{'form':form})

def post_course(request):
    if request.method =="POST":
	form = CourseForm(request.POST)
	if form.is_valid():
	    post = form.save(commit=False)
	    post.author = request.user
	    #post.published_date = timezone.now()
	    post.save()
		    #return redirect('tripadvise.views.post_detail.html',)
    else:
	form = CourseForm()
    return render(request, 'tripadvise/post_course.html', {'form': form})	
	

#def post_edit(request, pk):
    #post = get_object_or_404(Lodge, pk=pk)
    #if request.method == "POST":
        #form = LodgeForm(request.POST, instance=post)
        #if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            #return redirect('tripadvise.views.post_detail', pk=post.pk)
    #else:
        #form = LodgeForm(instance=post)
    #return render(request, 'tripadvise/post_edit.html', {'form': form})

