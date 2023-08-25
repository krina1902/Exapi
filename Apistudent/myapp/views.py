from django.shortcuts import render
from rest_framework import generics
from .models import Faculty,Student
from .serializers import FacultySerializer,StudentSerializer

# Create your views here.

class FacultyList(generics.ListCreateAPIView):
	queryset=Faculty.objects.all()
	serializer_class=FacultySerializer

class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Faculty
	serializer_class=FacultySerializer

class StudentList(generics.ListCreateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Student
	serializer_class=StudentSerializer
