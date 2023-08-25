from django.db import models

# Create your models here.

class Faculty (models.Model):
	fname=models.CharField(max_length=100,blank=True)
	lname=models.CharField(max_length=100,blank=True)
	email=models.EmailField(blank=True)
	course=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.fname 

class Student(models.Model):
	faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
	sfname=models.CharField(max_length=100,blank=True)
	slname=models.CharField(max_length=100,blank=True)
	mobile=models.PositiveSmallIntegerField(blank=True)

	def __str__(self):
		return self.sfname 
