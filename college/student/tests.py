from django.test import TestCase

from .models import (Student,Department)

import datetime
# Create your tests here.

class StudentModelTestCase(TestCase):

    def setUp(self) -> None:
        Student.objects.create(student_id='1234',student_name='gopichand',student_email='gopichand@gmail.com', student_dob=datetime.datetime.today())

    def testData(self):
        name = Student.objects.get(student_name='gopichand');
        self.assertEqual("1234",str(name))

class DepartmentModelTestCase(TestCase):

    def setUp(self) -> None:
        student_id = Student.objects.create(student_name='gopichand',student_email='gopichand@gmail.com', student_dob=datetime.datetime.today())
        Department.objects.create(student_id = student_id, department_name = 'ECE')
    def testData(self):
        department_name = Department.objects.get(department_name = 'ECE')

