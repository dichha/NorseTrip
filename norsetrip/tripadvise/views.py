from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import View
from django.contrib.auth import (
	logout as auth_logout, update_session_auth_hash,
)
from datetime import datetime
from django.core.urlresolvers import reverse
from django_ajax.decorators import ajax

from .models import Lodge, Course, Course_Lodge_Assignment, User, Course_User_Assignment, Review

from .forms import LodgeForm, CourseForm, Course_Lodge_AssignmentForm, UserForm, Course_User_AssignmentForm, ReviewForm
import collections




def home(request):
    return render(request, 'tripadvise/home.html')


def courses(request):
    courses = Course.objects.all()


    # paginator = Paginator(course_list, 6) # Show 6 lodges per page
    # page_request_var = "course_page"
    # page = request.GET.get(page_request_var)
    # try:
    #     course = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     course = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     course = paginator.page(paginator.num_pages)

    context = {
    'courses' : courses,
    # 'page_request_var': page_request_var,
    'title':'Courses For Study Abroad Program',
  
   

    }
    return render(request, 'tripadvise/courses.html', context )

def course_detail(request, courseId):
    course_info = get_object_or_404(Course, pk = courseId)
    cl_assign = Course_Lodge_Assignment.objects.all()
    lodges = Lodge.objects.all()

    class_color=""
    course_name=""
    if course_info.term == "JTERM":
        class_color = "jterm_course"
        course_name = "jcourse_name"
    elif course_info.term == "YEAR":
        class_color = "year_course"
        course_name = "ycourse_name"
    else:
        class_color = "semester_course"
        course_name = "scourse_name"
    


    context = {
    'course_info':course_info,
    'cl_assign': cl_assign,
    'lodges' : lodges,
    'class_color' : class_color,
    'course_name': course_name
    }
    return render(request, 'tripadvise/course_detail.html', context)


	
def hotels(request):
    lodge_list = Lodge.objects.all()
    review_list = Review.objects.all()
    # lodge_review_dict = {}
    # review_count = []

    # for lodge in lodge_list:
    #     lodge_review_dict[lodge.lodge_name] = lodge.review_set.count

    # sorted_hotels = collections.OrderedDict(sorted(lodge_review_dict.items(),key = lambda x: x[0]))

   

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
    'title': 'Accomodations Used in Study Abroad Courses',
    'lodge_list': lodge_list
    # 'sorted_hotels': sorted_hotels

    }

    return render(request, 'tripadvise/hotels.html', 
        context)


def hotel_details(request,lodgeId):
    #hotel info  
    cl_assign = Course_Lodge_Assignment.objects.all()
    courses = Course.objects.all()
    lodges = Lodge.objects.all()  
    lodge_info = get_object_or_404(Lodge,pk = lodgeId)
    unique_hotel_list=[]

    #reviews = Review.objects.all()
    reviews_list = Review.objects.filter(lodge_Id = lodge_info.lodgeId)

    paginator = Paginator(reviews_list,6) # Show 6 lodges per page
    page_request_var = "review_page"
    page = request.GET.get(page_request_var)
    try:
        review_pag = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        review_pag = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        review_pag = paginator.page(paginator.num_pages)

    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.lodge_Id = lodge_info
            review.rating = rating
            review.comment = comment
            review.pub_date = datetime.now()
            review.save()
            #always return an HTTPResponseRedirect after successfully dealing with POST data.This prevents data from being posted twice if a user hits the back button

            return HttpResponseRedirect(reverse('tripadvise.views.hotel_details', args = [str(lodge_info.lodgeId)]))
    else: 
        form = ReviewForm()
    #Trying using ajax
    # if request.method == 'POST':
    #     post_comment = request.POST.get('')
    unique_hotel_list=[]
    unique_hotel_course_dict = {}

    for cla in cl_assign:
        if lodge_info.lodge_name == str(cla.lodge_name):
            course_for_lodge = str(cla.course_name)
            for course in courses:
                if course.name == course_for_lodge:
                    for cla in cl_assign:
                        if(str(cla.course_name) == course.name):
                            if (str(cla.lodge_name) != lodge_info.lodge_name):
                                hotel_stayed = str(cla.lodge_name)
                                for lodge in lodges:
                                    if ((lodge.lodge_name == hotel_stayed) and (hotel_stayed not in unique_hotel_list)):
                                        unique_hotel_list.append(lodge.lodge_name)
                                        unique_hotel_course_dict[str(cla.course_name)] = lodge.lodge_name




    
    context = {
    'lodge_info':lodge_info,
    'cl_assign': cl_assign,
    'courses' : courses,
    'lodges' : lodges,
    # 'reviews' : reviews,
    'unique_hotel_list': unique_hotel_list,
    'form' : form,
    'review_pag' : review_pag,
    'page_request_var': page_request_var,
    'unique_hotel_list': unique_hotel_list,
    'unique_hotel_course_dict': unique_hotel_course_dict
    }

   
    return render(request,'tripadvise/hotel_details.html', context)

    

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
            #form = Course_Lodge_AssignmentForm()
            success = True
            #message success
            messages.success(request, "Successfully Assigned.")
           
        else:
            messages.error(request, "Not Successfully Assigned.")
	    
    else:
    	form = Course_Lodge_AssignmentForm()

    return render(request, 'tripadvise/clAssignment.html',{'form':form})


def post_course(request):
    if request.method == "POST":
        #request.POST or None is builtin validation
        form = CourseForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect(post.get_absolute_url())
        
    else:
    	form = CourseForm()
    return render(request, 'tripadvise/post_course.html', {'form': form})	


def post_user(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect(user.get_absolute_url())
        else:
            messages.error(request, "Not Successfully Created")
    else:
        form = UserForm()
    return render(request, 'tripadvise/post_user.html', {'form':form})

def users(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 6) # Show 6 lodges per page
    page_request_var = "lodge_page"
    page = request.GET.get(page_request_var)
    try:
        user = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        user = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        user = paginator.page(paginator.num_pages)

    context = {
    'user': user, 
    'page_request_var': page_request_var,
    'title': 'User'
    }

    return render(request, 'tripadvise/user.html', context)



def user_detail(request, userId):
    user_info = get_object_or_404(User,pk = userId)
    cu_assign = Course_User_Assignment.objects.all()
    courses = Course.objects.all()
    context = {
    'user_info': user_info,
    'cu_assign': cu_assign,
    'courses' : courses,

    }
    return render(request, 'tripadvise/user_detail.html', context)

def user_update(request, courseId = None):
    user = get_object_or_404(User, pk = courseId)
    form = UserForm(request.POST or None, instance = user)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(user.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Updated")
      
    context = {
      "user": user,
      "form": form

    }
    
    return render(request, 'tripadvise/post_user.html', context)

def cuAssignment(request):
    if request.method == "POST":
        form = Course_User_AssignmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = Course_User_AssignmentForm()
            success = True
            #message success
            messages.success(request, "Successfully Assigned.")
           
        else:
            messages.error(request, "Not Successfully Assigned.")
        
    else:
        form = Course_User_AssignmentForm()

    return render(request, 'tripadvise/cuAssignment.html',{'form':form})



	
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
    else:
        messages.error(request, "Not Successfully Updated")
      
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

def user_delete(request, userId = None):
    user = get_object_or_404(User, pk = userId)
    user.delete()
    messages.success(request, "Successfully deleted")
    return redirect("tripadvise.views.users")

def add_like(request):
    reviewid = None
    if request.method == 'GET':
        reviewid = request.GET['reviewId']

    likes = 0
    if reviewid:
        review = Review.objects.get(pk = (int(reviewid)))
        if review:
            likes = review.likes + 1
            review.likes = likes
            review.save()
    return HttpResponse(likes)

