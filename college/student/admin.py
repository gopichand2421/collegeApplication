from django.contrib import admin
from .models import  (Student,Department)


@admin.register(Student, Department)
class CollegeAdmin(admin.ModelAdmin):
    pass


# Register your models here.
