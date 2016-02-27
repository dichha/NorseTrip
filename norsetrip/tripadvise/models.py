from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse



class Lodge(models.Model):
	def __int__(self):
		return self.lodgeId
		
	def __str__(self):
		return self.lodge_name

	lodgeId = models.AutoField(primary_key = True,db_column = "LodgeId")	
	lodge_name = models.CharField(max_length = 200,db_column = "Name")
	lodge_address = models.CharField(max_length = 200, db_column = "Address")
	city = models.CharField(max_length = 100, db_column = "City")
	country = CountryField(blank_label = 'Select Country')
	lodge_url = models.URLField(db_column = "URL")
	lodge_descrip = models.TextField(db_column = "Description")
	average_rating = models.IntegerField(db_column = "Average Rating", default = 100)

	lodge_image = models.ImageField(null=True, blank = True,width_field = "width_field", 
		height_field = "height_field")

	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)

	def get_absolute_url(self):
		return reverse('tripadvise.views.hotel_details', args=[str(self.lodgeId)])

	#new lodge in the beginning	
	class Meta:
		ordering = ["-lodgeId"]


class Course(models.Model):
	def __int__(self):
		return self.courseId

	def __str__(self):
		return self.name	


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

	courseId = models.IntegerField(primary_key = True, db_column = "CourseId")
	name = models.CharField(max_length = 200, db_column = "Name")
	
	dept = models.CharField(max_length = 200, db_column = "Department", choices = DEPT)
	prof = models.CharField(max_length = 200, db_column = "Professor")
	year_offered = models.IntegerField(db_column = "Year Offered")
	course_lodge_assignments = models.ManyToManyField(Lodge,through='Course_Lodge_Assignment')
	term = models.CharField(max_length = 8, choices = TERM, default = 'JTERM')
	course_description = models.TextField(db_column = "Desciption", null = True )

	def get_absolute_url(self):
		return reverse('tripadvise.views.course_detail',args=[str(self.courseId)])
	

class Course_Lodge_Assignment(models.Model):
	def __int__(self):
		return self.clAssignId

	clAssignId = models.AutoField(primary_key= True, db_column="CourseLodgeAssignId")
	lodge_name = models.ForeignKey(Lodge, on_delete=models.CASCADE)
	course_name = models.ForeignKey(Course, on_delete=models.CASCADE)



	
class User(models.Model):
	def __int__(self):
		return self.userId

	def __str__(self):
		return self.email

	userId =  models.AutoField(primary_key = True, db_column = "UserId")
	email = models.EmailField(db_column = "Email", max_length = 24)

	ROLE_CHOICES = (('PROFESSOR', 'PROFESSOR'),
	                ('STUDENT','STUDENT'),
	                ('ALUMNI', 'ALUMNI'),
	                ('FACULTY', 'FACULTY'),
                )
	role = models.CharField(max_length = 9, choices = ROLE_CHOICES, db_column = "ROLE")

class Review(models.Model):
	def __int__(self):
		return self.reviewId
	
	reviewId = models.AutoField(primary_key = True, db_column = "ReviewId")
	lodge_Id = models.ForeignKey(Lodge, db_column = "LodgeID FK")
	user_Id = models.ForeignKey(User, db_column = "UserId FK")
	ONE = '1'
	TWO = '2'
	THREE = '3'
	FOUR = '4'
	FIVE = '5'
	
	RATING_CHOICES = ((ONE,"1"),
	                  (TWO,"2"),
	                  (THREE,"3"),
	                  (FOUR,"4"),
	                  (FIVE,"5"),
                )
	rating = models.CharField(choices = RATING_CHOICES, db_column = "Rating", max_length = 1)
	VC = '1'
	PC = '2'
	AVG = '3'
	PE = '4'
	VE = '5'
	COST_CHOICES = ((VC, "Very Cheap"),
	                (PC, "Pretty Cheap"),
	                (AVG, "Average"),
	                (PE, "Pretty Expensive"),
	                (VE, "Very Expensive"),
                )
	cost = models.CharField(choices = COST_CHOICES, db_column = "Cost", max_length = 16)
	comment = models.TextField(db_column = "Comment")
	pub_date = models.DateTimeField(db_column = "Date")

class Course_Assignment(models.Model):
	def __int__(self):
		return self.courseAssignId


	courseAssignId = models.AutoField(primary_key = True, db_column = "Course_AssignmentId")
	course_Id = models.ForeignKey(Course, db_column = "CourseId FK")
	user_Id = models.ForeignKey(User, db_column = "UserId FK")















