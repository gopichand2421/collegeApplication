from rest_framework import serializers

from .models import (Student,Department)

class StudentSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id','student_name','student_email','student_dob']

class DepartmentSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['department_id','student_id','department_name']