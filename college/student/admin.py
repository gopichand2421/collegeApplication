from django.contrib import admin
from .models import  (Student,Department, Subjects)


@admin.register(Student, Department, Subjects)
class CollegeAdmin(admin.ModelAdmin):
    pass


# Register your models here.
