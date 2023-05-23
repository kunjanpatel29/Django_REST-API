from django.db import models

# Create your models here.

class Student(models.Model):
	fname=models.CharField(max_length=100,blank=True)
	lname=models.CharField(max_length=100,blank=True)	
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	age=models.PositiveIntegerField()
	course=models.CharField(max_length=100,blank=True)
	fees=models.PositiveIntegerField()

	def __str__(self):
		return self.fname +" "+ self.lname