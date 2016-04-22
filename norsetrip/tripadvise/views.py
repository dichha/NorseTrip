from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import View
from django.contrib.auth import (
	logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from django.core.urlresolvers import reverse
from django_ajax.decorators import ajax

from tripadvise.models import Lodge, Course, Course_Lodge_Assignment, CustomUser, Course_User_Assignment, Review, Food, FoodReview

from .forms import LodgeForm, CourseForm, Course_Lodge_AssignmentForm, CustomUserForm, Course_User_AssignmentForm, ReviewForm, FoodForm, FoodReviewForm
import collections
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail


content_type = ContentType.objects.get_for_model(Review)


def index(request):
    reviewcontenttype = content_type
    if request.user and request.user.is_active:
        hello = 'hello'
        
        try:
            localemail = get_object_or_404(User, email = request.user.email)
            localuser = CustomUser.objects.get(email=localemail)
        except CustomUser.DoesNotExist:
            #localuser = CustomUser.objects.get(email=localemail)
            hello = 'hello'
        #permission = Permission.objects.get(codename='can_review', name = 'Can Review Lodges', content_type = reviewcontenttype)
        
        #localemail.user_permissions.add(permission)
        
        context = {
                    'localemail': localemail,
                    #'localuser': localuser,
                    'reviewcontenttype': reviewcontenttype,
                    }
                    
        return render(request, 'tripadvise/index.html')
    else:
        goodbye = 'goodbye'
        context = {
                    'reviewcontenttype': reviewcontenttype,
                    'goodbye': goodbye,
                }
        return render(request, 'tripadvise/index.html', context)

#@login_required
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

#@login_required
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
    requirements = course_info.rqmt
    


    context = {
    'course_info': course_info,
    'cl_assign': cl_assign,
    'lodges': lodges,
    'class_color': class_color,
    'course_name': course_name,
    'requirements': course_info.rqmt
    }
    return render(request, 'tripadvise/course_detail.html', context)


#@login_required	
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

def food_detail(request, foodId):
    
    food_info = get_object_or_404(Food, pk = foodId)
    foodreview = FoodReview.objects.all()
    
    if request.user.is_active:
	author = request.user.email
	customuser = CustomUser.objects.get(email = author)
	userid = customuser.userId  
	
    reviews_list = FoodReview.objects.filter(food_Id = food_info.foodId)
	
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
	form = FoodReviewForm(request.POST or None)
	if form.is_valid():
		rating = form.cleaned_data['rating']
		comment = form.cleaned_data['comment']
		review = FoodReview()
		review.food_Id = food_info
		review.user_Id = customuser
		review.author = author
		review.rating = rating
		review.comment = comment
		review.pub_date = datetime.now()
		reviewcontenttype = content_type
		if request.user and request.user.is_active:
		    try:
			localemail = get_object_or_404(User, email = request.user.email)
			foodcheck = Course_Lodge_Assignment.objects.filter(lodge_name__city = review.food_Id.city)
			#citycheck = Lodge.objects.get(city = foodcheck)
			getlodgeId = Course_Lodge_Assignment.objects.get(clAssignId = foodcheck)
			#getlodge = Lodge.objects.filter(lodgeId = citycheck)
			#getclId = Course_Lodge_Assignment.objects.filter(clAssignId = getlodge)
			getcourse = Course.objects.get(course_lodge_assignment__clAssignId = getlodgeId)
			
			localuser = Course_User_Assignment.objects.get(user_Id__email=localemail,course_Id__name__icontains=getcourse)
			#get the city that is in lodge that is the same in food
			#then get the courses that is with that lodge
			#then make sure that this user is assigned that same course
			#then this user can write the review
			#foodcheck = Food.objects.get(name__icontains = foodreview.food_Id)
		    except Course_User_Assignment.DoesNotExist:
			return render(request, 'tripadvise/notauser.html')
		        permission = Permission.objects.get(codename = 'can_review', content_type = foodreviewcontenttype)
		        localemail.user_permissions.add(permission)
		else:
		    return render(request, 'tripadvise/notauser.html')
					
		review.save()
		return HttpResponseRedirect(reverse('tripadvise.views.food_detail', args = [str(food_info.foodId)]))
    else: 
	form = FoodReviewForm() 	    
		
    context = {
        'food_info': food_info,
        'form': form,
        #'foodreviews_list': foodreviews_list,
        
        'page_request_var': page_request_var,
        'review_pag' : review_pag,
        
        }
    return render(request, 'tripadvise/food_detail.html', context)

#@login_required	

def hotel_details(request,lodgeId):
    #hotel info  
    cl_assign = Course_Lodge_Assignment.objects.all()
    courses = Course.objects.all()
    foods = Food.objects.all()
    
    lodges = Lodge.objects.all()  
    lodge_info = get_object_or_404(Lodge,pk = lodgeId)
    unique_hotel_list=[]
    
    if request.user.is_active:
    	try:
	    author = request.user.email
	    customuser = CustomUser.objects.get(email = author)
	    userid = customuser.userId
	except CustomUser.DoesNotExist:
	    pass
    else:
	pass

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
            review.user_Id = customuser
            review.author = author
            review.rating = rating
            review.comment = comment
            review.pub_date = datetime.now()
            reviewcontenttype = content_type
            if request.user and request.user.is_active:
            	try:
            		localemail = get_object_or_404(User, email = request.user.email)
			#lodgecheck = Lodge.objects.get(lodge_name__icontains = review.lodge_Id)
			lodgecheck = Course_Lodge_Assignment.objects.filter(lodge_name = review.lodge_Id)
			#coursecheck = Course_Lodge_Assignment.objects.filter(lodge_name=lodgecheck)
			getclid = Course_Lodge_Assignment.objects.filter(clAssignId = lodgecheck)
			#getclid = Course_Lodge_Assignment.objects.filter(clAssignId=coursecheck)			
			
			getcourse = Course.objects.get(course_lodge_assignment__clAssignId=getclid)
			#getcoursenow = 
			getcoursenow = Course_Lodge_Assignment.objects.filter(course_name = getcourse)	
			localuser = Course_User_Assignment.objects.get(user_Id__email=localemail,course_Id__name__icontains=getcourse)
			#localcourse = Course_User_Assignment.objects.get(course_Id__name=getcourse)
            	except Course_User_Assignment.DoesNotExist:
            		return render(request, 'tripadvise/notauser.html')
            		permission = Permission.objects.get(codename = 'can_review', content_type = reviewcontenttype)
            		localemail.user_permissions.add(permission)
            else:
            	return render(request, 'tripadvise/notauser.html')
            	
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
    'foods' : foods,
    # 'reviews' : reviews,
    'unique_hotel_list': unique_hotel_list,
    'form' : form,
    'review_pag' : review_pag,
    'page_request_var': page_request_var,
    'unique_hotel_list': unique_hotel_list,
    'unique_hotel_course_dict': unique_hotel_course_dict
    }

   
    return render(request,'tripadvise/hotel_details.html', context)

    
@staff_member_required
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

@staff_member_required    
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

@staff_member_required
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

def post_food(request):
    foods = Food.objects.all()
    
    #food_info = get_object_or_404(Food,pk = foodId)
    
    if request.method == "POST":
	#request.POST or None is builtin validation
	form = FoodForm(request.POST or None)
	if form.is_valid():
	    #food = Food()
	    #food.city = city 
	    post = form.save(commit=False)
	    #food = get_object_or_404(Food, foodId = city)
	    #review.lodge_Id = lodge_info
	    #review.user_Id = customuser
	    #review.author = author
	    #review.rating = rating
	    #review.comment = comment.city = city
	    if request.user and request.user.is_active:
		try:
		    localemail = get_object_or_404(User, email = request.user.email)
		    
		    localuser = CustomUser.objects.get(email = localemail)
		except CustomUser.DoesNotExist:
		    return render(request, 'tripadvise/notauser.html')
		#try:
		    #localemail = get_object_or_404(User, email = request.user.email)
		    #getcity = Course_Lodge_Assignment.objects.get(lodge_name__city = city)
		    #getclid = Course_Lodge_Assignment.objects.get(clAssignId = getcity)
		    #getcourse = Course.objects.get(course_lodge_assignment__course_name = getclid)
		    
		    #localtruth = Course_User_Assignment.objects.get(user_Id__email=localemail,course_Id__name__icontains=getcourse)
		#except Course_User_Assignment.DoesNotExist:
		    #return render(request, 'tripadvise/notavalidfood.html')
	    else:
		return render(request, 'tripadvise/notauser.html')
	    post.save()
	    messages.success(request, "Successfully Created")
	    return HttpResponseRedirect(post.get_absolute_url())
	    
    else:
	form = FoodForm()
    context = {
        #'food': food,
        #'food_info': food_info,
        'form' : form,
        }
    return render(request, 'tripadvise/post_food.html', context) 

def food_update(request, foodId = None):
    foods = get_object_or_404(Food, pk = foodId)
    form = FoodForm(request.POST or None, instance = foods)
    if form.is_valid():
        foods = form.save(commit=False)
        foods.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(foods.get_absolute_url())
    
    context = {
      "foods": foods,
      "form": form

    }
    
    return render(request, 'tripadvise/post_food.html', context)
def food_delete(request, foodId = None):
    food = get_object_or_404(Food, pk = foodId)
    food.delete()
    messages.success(request, "Successfully deleted")
    return redirect("tripadvise.views.hotels")

@staff_member_required
def post_user(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect(user.get_absolute_url())
        else:
            messages.error(request, "Not Successfully Created")
    else:
        form = CustomUserForm()
    return render(request, 'tripadvise/post_user.html', {'form':form})

@staff_member_required
def users(request):
    #user_list = User.objects.all()
    student_list = CustomUser.objects.filter(role = "STUDENT")
    prof_list = CustomUser.objects.filter(role = "PROFESSOR")
    fac_list = CustomUser.objects.filter(role = "FACULTY")


    # pagination for students
    paginator = Paginator(student_list, 12) # Show 6 lodges per page
    page_request_var1 = "stu_page"
    page1 = request.GET.get(page_request_var1)
    try:
        students = paginator.page(page1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    # pagination for professors
    paginator = Paginator(prof_list, 12) # Show 6 lodges per page
    page_request_var2 = "prof_page"
    page2 = request.GET.get(page_request_var2)
    try:
        profs = paginator.page(page2)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        profs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        profs = paginator.page(paginator.num_pages)

    # pagination for faculty
    paginator = Paginator(fac_list, 12) # Show 6 lodges per page
    page_request_var3 = "fac_page"
    page3 = request.GET.get(page_request_var3)
    try:
        facs = paginator.page(page3)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        facs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        facs = paginator.page(paginator.num_pages)



    context = {
    # 'users': users,
    'students': students,
    'profs': profs,
    'facs': facs, 
    'page_request_var1': page_request_var1,
    'page_request_var2': page_request_var2,
    'page_request_var3': page_request_var3,
    'title': 'Registered Users'
    }

    return render(request, 'tripadvise/user.html', context)

@staff_member_required
def user_detail(request, userId):
    user_info = get_object_or_404(CustomUser,pk = userId)
    customuser = CustomUser.objects.get(userId = userId)
    cu_assign = Course_User_Assignment.objects.all()
    courses = Course.objects.all()


    reviews_list = Review.objects.filter(user_Id = user_info.userId)

    paginator = Paginator(reviews_list,6) # Show 6 lodges per page
    page_request_var = "review_page"
    page = request.GET.get(page_request_var)
    try:
        user_review = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        user_review = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        user_review = paginator.page(paginator.num_pages)
    
    context = {
    'user_info': user_info,
    'cu_assign': cu_assign,
    'courses' : courses,
    'reviews_list' : reviews_list,
    'user_review': user_review

    }
    return render(request, 'tripadvise/user_detail.html', context)

@staff_member_required
def user_update(request, courseId = None):
    customuser = get_object_or_404(CustomUser, pk = courseId)
    form = CustomUserForm(request.POST or None, instance = customuser)
    if form.is_valid():
        customuser = form.save(commit=False)
        customuser.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(customuser.get_absolute_url())
      
    context = {
      "customuser": customuser,
      "form": form

    }
    
    return render(request, 'tripadvise/post_user.html', context)

@staff_member_required
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

def login_error(request):
	logger.debug("Login Error")
	return HttpResponseRedirect("/login-error.html")

	
def logout_view(request):
	logger.debug("Logout called by user")
	logout(request)
	return HttpResponseRedirect("/")

@staff_member_required
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

@staff_member_required
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

@staff_member_required
def course_delete(request, courseId = None):
    course = get_object_or_404(Course, pk = courseId)
    course.delete()
    messages.success(request, "Successfully deleted")
    return redirect("tripadvise.views.courses")

@staff_member_required
def hotel_delete(request, lodgeId = None):
    lodge = get_object_or_404(Lodge, pk = lodgeId)
    lodge.delete()
    messages.success(request, "Successfully deleted")
    return redirect("tripadvise.views.hotels")

@staff_member_required
def user_delete(request, userId = None):
    user = get_object_or_404(CustomUser, pk = userId)
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

