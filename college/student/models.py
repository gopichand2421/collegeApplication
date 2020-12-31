from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(max_length=11,null=False, primary_key = True)
    student_name = models.CharField(max_length=250, blank=False)
    student_email = models.EmailField(max_length=250)
    student_dob = models.DateField()
    # studend_dob = models.DateField()

    class Meta:
        ordering = ('student_id',)

    def __str__(self):
        return str(self.student_id)

    def __unicode__(self):
        return str(self.student_id)

class Department(models.Model):
    department_id = models.AutoField(primary_key = True)
    student_id = models.ForeignKey(Student, on_delete= models.CASCADE)
    department_name = models.CharField(max_length=250, blank=False)

    class Meta:
        ordering = ('department_name',)

    def __str__(self):
        self.department_name

    def __unicode__(self):
        self.department_name