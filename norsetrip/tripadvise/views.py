
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views.generic import View

from django.shortcuts import redirect

from .models import Lodge

from .models import Course

from .models import Course_Lodge_Assignment

from .forms import LodgeForm

from .forms import Course_Lodge_AssignmentForm

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

def course_detail(request, courseId):
    course_info = get_object_or_404(Course, pk = courseId)
    return render(request, 'tripadvise/course_detail.html', {'course_info': course_info})


	
def hotels(request):
    lodge_list = Lodge.objects.all()
    paginator = Paginator(lodge_list, 6) # Show 5 lodges per page
    page_request_var = "lodge_page"
    page = request.GET.get(page_request_var)
    try:
        lodge = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lodge = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lodge = paginator.page(paginator.num_pages)

    context = {
    'lodge': lodge, 
    'page_request_var': page_request_var,
    'title': 'Hotel'
    }

    return render(request, 'tripadvise/hotels.html', context)


#def course_lodge_assignment(request):
 #   course_lodge = Lodge.objects.()
def hotel_details(request,lodgeId):
    lodge_info = get_object_or_404(Lodge,pk = lodgeId)
    return render(request,'tripadvise/hotel_details.html',{'lodge_info':lodge_info})
    

def post_lodge(request):
    if request.method == "POST":

        form = LodgeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #message success
            messages.success(request, "Successfully Created!")
            return HttpResponseRedirect(post.get_absolute_url())
        else:
            messages.error(request, "Not Successfully Created.")
    else:
        form = LodgeForm()
    return render(request, 'tripadvise/post_lodge.html', {'form': form})
def courseLodgeAssign_new(request):
    if request.method == "POST":
    	form = Course_Lodge_AssignmentForm(request.POST)
    	if form.is_valid():
    	    post = form.save(commit=False)
    	    post.save()
	    
    else:
    	form = Course_Lodge_AssignmentForm()

    return render(request, 'tripadvise/new_clAssign.html',{'form':form})

def post_course(request):
    if request.method =="POST":
        #request.POST or None is builtin validation
        form = CourseForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect(post.get_absolute_url())
        else:
            messages.error(request, "Not Successfully Created")
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

