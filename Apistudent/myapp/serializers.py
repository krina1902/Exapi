from rest_framework import serializers
from .models import Faculty,Student

class FacultySerializer(serializers.ModelSerializer):
	class Meta:
		model=Faculty
		fields=('id','fname','lname','email','course')


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Student
		fields=('id','faculty','sfname','slname','mobile')