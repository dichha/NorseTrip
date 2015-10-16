from django.db import models

# Create your models here.
class Lodging(models.Model):
	def __str__(self):
		return self.lodge_name

	#def __str__(self):
	#	return self.lodge_address

	# def __str__(self):
	# 	return city

	lodge_name = models.CharField(max_length = 200,db_column = "Name")
 	#course_Id = models.ForeignKey(Course,verbose_name = "course_id")
 	lodge_address = models.CharField(max_length = 200, db_column = "Address")
 	city = models.CharField(max_length = 100, db_column = "City")
 	country = models.CharField(max_length = 100, db_column = "Country")
 	pub_date = models.DateTimeField(db_column = "Date");