from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentList(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student
	serializer_class = StudentSerializer
