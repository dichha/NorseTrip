from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import View
from django.contrib.auth import (
	logout as auth_logout, update_session_auth_hash,
)

from .models import Lodge
from .models import Course
from .models import Course_Lodge_Assignment

from .forms import LodgeForm
from .forms import CourseForm
from .forms import Course_Lodge_AssignmentForm



def home(request):
    return render(request, 'tripadvise/home.html')


def courses(request):
    course_list = Course.objects.all()
    paginator = Paginator(course_list, 6) # Show 6 lodges per page
    page_request_var = "course_page"
    page = request.GET.get(page_request_var)
    try:
        course = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        course = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        course = paginator.page(paginator.num_pages)

    context = {
    'course' : course,
    'page_request_var': page_request_var

    }
    return render(request, 'tripadvise/courses.html', context )

def course_detail(request, courseId):
    course_info = get_object_or_404(Course, pk = courseId)
    cl_assign = Course_Lodge_Assignment.objects.all()
    lodges = Lodge.objects.all()
    context = {
    'course_info':course_info,
    'cl_assign': cl_assign,
    'lodges' : lodges
    }
    return render(request, 'tripadvise/course_detail.html', context)


	
def hotels(request):
    lodge_list = Lodge.objects.all()
    paginator = Paginator(lodge_list, 6) # Show 6 lodges per page
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


def hotel_details(request,lodgeId):
    lodge_info = get_object_or_404(Lodge,pk = lodgeId)
    cl_assign = Course_Lodge_Assignment.objects.all()
    courses = Course.objects.all()
    context = {
    'lodge_info':lodge_info,
    'cl_assign': cl_assign,
    'courses' : courses
    }

    return render(request,'tripadvise/hotel_details.html',context)
    

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
def clAssignment(request):
    if request.method == "POST":
    	form = Course_Lodge_AssignmentForm(request.POST)
    	if form.is_valid():
    	    post = form.save(commit=False)
    	    post.save()
            form = Course_Lodge_AssignmentForm()
            success = True
            #message success
            messages.success(request, "Successfully Assigned.")
           
        else:
            messages.error(request, "Not Successfully Assigned.")
	    
    else:
    	form = Course_Lodge_AssignmentForm()

    return render(request, 'tripadvise/clAssignment.html',{'form':form})

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
	
def logout_view(request):
	logger.debug("Logout called by user")
	logout(request)
	return HttpResponseRedirect("/")


def lodge_update(request, lodgeId = None):
    lodges = get_object_or_404(Lodge, pk = lodgeId)
    form = LodgeForm(request.POST or None, instance = lodges)
    if form.is_valid():
        lodges = form.save(commit=False)
        lodges.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(lodges.get_absolute_url())
    # else:
    #     messages.error(request, "Not Successfully Updated")
      
    context = {
      "lodges": lodges,
      "form": form

    }
    
    return render(request, 'tripadvise/post_lodge.html', context)


def course_update(request, courseId = None):
    courses = get_object_or_404(Course, pk = courseId)
    form = CourseForm(request.POST or None, instance = courses)
    if form.is_valid():
        courses = form.save(commit=False)
        courses.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(courses.get_absolute_url())
    # else:
    #     messages.error(request, "Not Successfully Updated")
      
    context = {
      "courses": courses,
      "form": form

    }

    
    return render(request, 'tripadvise/post_course.html', context)

def course_delete(request, courseId = None):
    course = get_object_or_404(Course, pk = courseId)
    course.delete()
    messages.success(request, "Successfully deleted")
    return redirect("tripadvise.views.courses")

def hotel_delete(request, lodgeId = None):
    lodge = get_object_or_404(Lodge, pk = lodgeId)
    lodge.delete()
    messages.success(request, "Successfully deleted")
    return redirect("tripadvise.views.hotels")


