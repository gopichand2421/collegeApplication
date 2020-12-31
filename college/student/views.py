from django.shortcuts import render
from rest_framework import viewsets
from .models import Student,Department
from .serilizers import StudentSerilizer,DepartmentSerilizer
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerilizer