from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse
import numpy as np
import datetime


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
	lodge_image = models.ImageField("Lodge Image", null=True, blank = True,width_field = "width_field", 
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
		return np.mean(all_ratings)

class Review(models.Model):
	def __int__(self):
		return self.reviewId

	RATING_CHOICES = ((1, '1'),
					(2, '2'),
					(3, '3'),
					(4, '4'),
					(5, '5'),
                )
	
	reviewId = models.AutoField(primary_key = True)
	#many to one: many reviews to one lodge
	lodge_Id = models.ForeignKey(Lodge,on_delete = models.CASCADE)
	# user_Id = models.ForeignKey(User, db_column = "UserId FK")
	rating = models.IntegerField("Rating", choices = RATING_CHOICES)
	comment = models.TextField("Comment")
	pub_date = models.DateTimeField("Date Published")
	likes = models.IntegerField(default=0)

	class Meta:
		ordering = ["-pub_date"]


class Course(models.Model):
	def __int__(self):
		return self.courseId

	def __str__(self):
		return self.name

	YEAR_CHOICES = []
	for r in range(1990, (datetime.datetime.now().year+4)):
		YEAR_CHOICES.append((r,r))


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
	        ('PAIDIEA','PAIDIEA'),
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

	clAssignId = models.AutoField(primary_key= True, db_column="CourseLodgeAssignId")
	lodge_name = models.ForeignKey(Lodge, on_delete=models.CASCADE)
	course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

	class Meta:
		unique_together = ['lodge_name', 'course_name']

	
class User(models.Model):
	def __int__(self):
		return self.userId

	def __str__(self):
		return self.email

	userId =  models.AutoField(primary_key = True, db_column = "UserId")
	fullName = models.CharField("Full Name", max_length = 5)
	email = models.EmailField("Email", max_length = 24)

	ROLE_CHOICES = (('PROFESSOR', 'PROFESSOR'),
	                ('STUDENT','STUDENT'),
	                ('ALUMNI', 'ALUMNI'),
	                ('FACULTY', 'FACULTY'),
                )
	role = models.CharField("Role",choices = ROLE_CHOICES, max_length = 9)

	course_user_assignments = models.ManyToManyField(Course,through='Course_User_Assignment')

	def get_absolute_url(self):
		return reverse('tripadvise.views.user_detail',args=[str(self.userId)])





class Course_User_Assignment(models.Model):
	def __int__(self):
		return self.courseAssignId

	courseAssignId = models.AutoField(primary_key = True, db_column = "Course_AssignmentId")
	course_Id = models.ForeignKey(Course, db_column = "CourseId FK", on_delete=models.CASCADE)
	user_Id = models.ForeignKey(User, db_column = "UserId FK", on_delete=models.CASCADE)

	class Meta:
		unique_together = ["course_Id", "user_Id"]














