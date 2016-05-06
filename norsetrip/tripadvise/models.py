from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import numpy as np
import datetime
from multiselectfield import MultiSelectField


class Lodge(models.Model):
	def __int__(self):
		return self.lodgeId
		
	def __str__(self):
		return self.lodge_name

	lodgeId = models.AutoField("LodgeId", primary_key = True)	
	lodge_name = models.CharField("Name", max_length = 200)
	lodge_address = models.CharField("Address", max_length = 200)
	city = models.CharField("City", max_length = 100)
	country = CountryField("Country", blank_label = 'Select Country')
	lodge_url = models.URLField("Lodge URL")
	lodge_descrip = models.TextField("Lodge Description")
	lodge_image = models.ImageField("Lodge Image", null=True, blank = False,width_field = "width_field", 
		height_field = "height_field")

	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)
	#lodge_review_assignment = models.

	def get_absolute_url(self):
		return reverse('tripadvise.views.hotel_details', args=[str(self.lodgeId)])

	#newly added lodge in the beginning	
	class Meta:
		ordering = ["lodge_name"]
		#preventing duplicates
		unique_together = ["lodge_name","lodge_address","city","country","lodge_url"]

	def mean_rating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return (np.mean(all_ratings)*20)



class Review(models.Model):
	def __int__(self):
		return self.reviewId
	def __unicode__(self):
		return '%s' % (self.reviewId)	

	RATING_CHOICES = ((1, '1'),
					(2, '2'),
					(3, '3'),
					(4, '4'),
					(5, '5'),
                )
	
	reviewId = models.AutoField(primary_key = True)
	#many to one: many reviews to one lodge
	lodge_Id = models.ForeignKey(Lodge,on_delete = models.CASCADE)
	user_Id = models.ForeignKey('CustomUser', db_column = "UserId FK", on_delete = models.CASCADE)
	author = models.EmailField("Author", max_length=24)
	rating = models.IntegerField("Rating", choices = RATING_CHOICES)
	comment = models.TextField("Comment")
	pub_date = models.DateTimeField("Date Published")
	likes = models.IntegerField(default=0)

	class Meta:
		ordering = ["-pub_date"]
	
	def get_absolute_url(self):
		return reverse('tripadvise.views.review_detail',args=[str(self.reviewId)])	


class Course(models.Model):
	def __int__(self):
		return self.courseId

	def __str__(self):
		return self.name

	YEAR_CHOICES = []
	for r in range(1990, (datetime.datetime.now().year+4)):
		YEAR_CHOICES.append((r,r))

	REQUIREMENTS = (('INTCL', 'INTERCULTURAL'),
					('HB', 'HUMAN BEHAVIOR'),
					('HBSSM','HUMAN EXPRESSION SOCIAL SCIENCE METHODS'),
					('HEPT', 'HUMAN EXPRESSION PRIMARY TEXT'),
					('HIST','HISTORICAL'),
					('JTERM II', 'SECOND JTERM'),
					('NOTTINGHAM','NOTTINGHAM'),
					('NWL','NATURAL WORLD LAB'),
					('NWNL','NATURAL WORLD NON LAB'),
					('QUANT','QUANTITAVE'),
					('REL II', 'RELIGION II'),
					('ROCHESTER', 'ROCHESTER'),	
					('PAID 450', 'PAIDEIA 450'),
					('WASHINGTON', 'WASHINGTON')
					)

		

	TERM = (
        ('JTERM','JTERM'),
        ('SUMMER','SUMMER'),
        ('YEAR','YEAR'),
        ('SEMESTER',"SEMESTER"),
        )

	DEPT = (('AFRICANA STUDIES', 'AFRICANA STUDIES'),
	        ('BIOLOGY', 'BIOLOGY'),
	        ('CHEMISTRY','CHEMISTRY'),
	        ('CLASSICS','CLASSICS'),
	        ('COMMUNICATION STUDIES', 'COMMUNICATION STUDIES'),
	        ('COMPUTER SCIENCE','COMPUTER SCIENCE'),
	        ('ECONOMICS AND BUSINESS','ECONOMICS AND BUSINESS'),
	        ('EDUCATION','EDUCATION'),
	        ('ENGLISH','ENGLISH'),
	        ('ENVIRONMENTAL STUDIES','ENVIRONMENTAL STUDIES'),
	        ('HEALTH AND PHYSICAL EDUCATION','HEALTH AND PHYSICAL EDUCATION'),
	        ('HISTORY','HISTORY'),
	        ('INTERNATIONAL STUDIES','INTERNATIONAL STUDIES'),
	        ('LIBRARY AND INFORMATION STUDIES','LIBRARY AND INFORMATION STUDIES'),
	        ('MATHEMATICS', 'MATHEMATICS'),
	        ('MODERN LANGUAGES, LITERATURES AND LINGUISTICS','MODERN LANGUAGES, LITERATURES AND LINGUISTICS'),
	        ('MUSEUM STUDIES','MUSEUM STUDIES'),
	        ('MUSIC','MUSIC'),
	        ('NURSING','NURSING'),
	        ('PAIDEIA','PAIDEIA'),
	        ('PHILOSOPHY','PHILOSOPHY'),
	        ('PHYSICS','PHYSICS'),
	        ('POLITICAL SCIENCE','POLITICAL SCIENCE'),
	        ('PSYCHOLOGY','PSYCHOLOGY'),
	        ('RELIGION','RELIGION'),
	        ('RUSSIAN STUDIES','RUSSIAN STUDIES'),
	        ('SCHOLARS PROGRAM','SCHOLARS PROGRAM'),
	        ('SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK', 'SOCIOLOGY/ANTHROPOLOGY/SOCIAL WORK'),
	        ('VISUAL AND PERFORMING ARTS','VISUAL AND PERFORMING ARTS'),
	        ('WOMEN AND GENDER STUDIES', 'WOMEN AND GENDER STUDIES'),


                )

	courseId = models.IntegerField("Course Id", primary_key = True, )
	name = models.CharField("Course Name", max_length = 200)
	
	dept = models.CharField("Department", max_length = 200,choices = DEPT)
	prof = models.CharField("Professor", max_length = 200)
	year_offered = models.IntegerField("Year Offered", choices = YEAR_CHOICES, default = datetime.datetime.now().year)

	course_lodge_assignments = models.ManyToManyField(Lodge,through='Course_Lodge_Assignment')
	term = models.CharField("Term Offered", max_length = 8, choices = TERM, default = 'JTERM')
	# rqmt = models.CharField("Requirement(s) Filled", max_length = 41, choices=REQUIREMENTS, default = 'INTCL')
	rqmt = MultiSelectField("Requirement(s) Filled", max_length = 41, choices=REQUIREMENTS, default = 'INTCL')
	course_description = models.TextField("Course Description", null = True )

	#newly added Course in the beginning
	class Meta:
		ordering = ["name"]
		# ordering = ["dept"]


	def get_absolute_url(self):
		return reverse('tripadvise.views.course_detail',args=[str(self.courseId)])
	

class Course_Lodge_Assignment(models.Model):
	def __int__(self):
		return self.clAssignId
	
	def __unicode__(self):
			return '%s' % (self.course_name)		

	clAssignId = models.AutoField(primary_key= True, db_column="CourseLodgeAssignId")
	lodge_name = models.ForeignKey(Lodge, on_delete=models.CASCADE)
	course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

	class Meta:
		unique_together = ['lodge_name', 'course_name']

	
class CustomUser(models.Model):
	def __int__(self):
		return self.userId

	def __str__(self):
		return self.email

	userId =  models.AutoField(primary_key = True, db_column = "UserId")
	fullName = models.CharField("Full Name", max_length = 50)
	email = models.EmailField("Email", max_length = 24)

	ROLE_CHOICES = (('STUDENT','STUDENT'),
					('PROFESSOR', 'PROFESSOR'),
	                ('ALUMNI', 'ALUMNI'),
	                ('FACULTY', 'FACULTY'),
                )
	role = models.CharField("Role",choices = ROLE_CHOICES, max_length = 9, default='STUDENT')

	course_user_assignments = models.ManyToManyField(Course,through='Course_User_Assignment')

	def get_absolute_url(self):
		return reverse('tripadvise.views.user_detail',args=[str(self.userId)])
	class Meta:
		ordering = ["fullName"]





class Course_User_Assignment(models.Model):
	def __int__(self):
		return self.courseAssignId
	def __unicode__(self):
		return '%s' % (self.course_Id)	
	

	courseAssignId = models.AutoField(primary_key = True, db_column = "Course_AssignmentId")
	course_Id = models.ForeignKey(Course, db_column = "CourseId FK", on_delete=models.CASCADE)
	user_Id = models.ForeignKey(CustomUser, db_column = "UserId FK", on_delete=models.CASCADE)

	class Meta:
		unique_together = ["course_Id", "user_Id"]
		
class Food(models.Model):
	def __int__(self):
		return self.foodId	
	def __str__(self):
		return self.name	
	
	foodId = models.AutoField(primary_key = True, db_column = "FoodId")
	user_Id = models.ForeignKey('CustomUser', db_column = "UserId FK", on_delete = models.CASCADE, null = True)
	name = models.CharField("Name", max_length = 200)
	author = models.EmailField("Author", max_length=24, null = True)	
	
	address = models.CharField("Address", max_length = 200)
	city = models.CharField("City", max_length = 100)
	country = CountryField("Country", blank_label = 'Select Country')
	url = models.URLField("Food URL", null = True, blank = True)
	descrip = models.TextField("Food Description")
	pub_date = models.DateTimeField("Date Published", null = True)
	image = models.ImageField("Food Image", null=True, blank = False, width_field = "width_field", 
		height_field = "height_field")
	#def save(self,force_insert=False, force_update=False, *args, **kwargs):
		#super(Food, self).save(force_insert, force_update)
		#if self.image:
			#if self.image.width > 300 or self.image.height > 300:
				#resize_image(self.image)	

	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)
	#def save(self,force_insert=False, force_update=False, *args, **kwargs):
		#super(Food, self).save(force_insert, force_update)
		#if self.image:
			#if self.image.width > 300 or self.image.height > 300:
				#resize_image(self.image)	
	
	def get_absolute_url(self):
		return reverse('tripadvise.views.food_detail', args=[str(self.foodId)])	
	
	class Meta:
		ordering = ["name"]
		#preventing duplicates
		unique_together = ["name","address","city","country", "url"]

	def mean_rating(self):
		all_ratings = map(lambda x: x.rating, self.foodreview_set.all())
		return (np.mean(all_ratings)*20)
	
	
class FoodReview(models.Model):
	def __int__(self):
		return self.reviewId
	def __unicode__(self):
		return '%s' % (self.reviewId)
	
	RATING_CHOICES = ((1,'1'),
                          (2,'2'),
                          (3, '3'),
                          (4, '4'),
                          (5, '5'),
        )
	
	reviewId = models.AutoField(primary_key = True)
	
	food_Id = models.ForeignKey(Food,on_delete  = models.CASCADE)
	user_Id = models.ForeignKey('CustomUser', db_column = "UserId FK", on_delete = models.CASCADE)
	author = models.EmailField("Author", max_length=24)
	rating = models.IntegerField("Rating", choices = RATING_CHOICES)
	comment = models.TextField("Comment")
	pub_date = models.DateTimeField("Date Published")
	likes = models.IntegerField(default=0)
	
	class Meta:
		ordering = ["-pub_date"]
		
class Entertainment(models.Model):
	def __int__(self):
		return self.funId	
	def __str__(self):
		return self.name	
	
	entertainmentId = models.AutoField(primary_key = True, db_column = "EntertainmentId")
	user_Id = models.ForeignKey('CustomUser', db_column = "UserId FK", on_delete = models.CASCADE, null = True)
	name = models.CharField("Name", max_length = 200)
	author = models.EmailField("Author", max_length=24, null = True)	
	
	address = models.CharField("Address", max_length = 200)
	city = models.CharField("City", max_length = 100)
	country = CountryField("Country", blank_label = 'Select Country')
	url = models.URLField("URL", null = True, blank = True)
	descrip = models.TextField("Entertainment Description")
	pub_date = models.DateTimeField("Date Published", null = True)
	image = models.ImageField("Entertainment Image", null=True, blank = False, width_field = "width_field", 
		height_field = "height_field")
	#def save(self,force_insert=False, force_update=False, *args, **kwargs):
		#super(Food, self).save(force_insert, force_update)
		#if self.image:
			#if self.image.width > 300 or self.image.height > 300:
				#resize_image(self.image)	

	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)
	#def save(self,force_insert=False, force_update=False, *args, **kwargs):
		#super(Food, self).save(force_insert, force_update)
		#if self.image:
			#if self.image.width > 300 or self.image.height > 300:
				#resize_image(self.image)	
	
	def get_absolute_url(self):
		return reverse('tripadvise.views.entertainment_detail', args=[str(self.entertainmentId)])	
	
	class Meta:
		ordering = ["name"]
		#preventing duplicates
		unique_together = ["name","address","city","country", "url"]

	def mean_rating(self):
		all_ratings = map(lambda x: x.rating, self.entertainmentreview_set.all())
		return (np.mean(all_ratings)*20)
	
	
class EntertainmentReview(models.Model):
	def __int__(self):
		return self.reviewId
	def __unicode__(self):
		return '%s' % (self.reviewId)
	
	RATING_CHOICES = ((1,'1'),
                          (2,'2'),
                          (3, '3'),
                          (4, '4'),
                          (5, '5'),
        )
	
	reviewId = models.AutoField(primary_key = True)
	
	entertainment_Id = models.ForeignKey(Entertainment,on_delete  = models.CASCADE)
	user_Id = models.ForeignKey('CustomUser', db_column = "UserId FK", on_delete = models.CASCADE)
	author = models.EmailField("Author", max_length=24)
	rating = models.IntegerField("Rating", choices = RATING_CHOICES)
	comment = models.TextField("Comment")
	pub_date = models.DateTimeField("Date Published")
	likes = models.IntegerField(default=0)
	
	class Meta:
		ordering = ["-pub_date"]

