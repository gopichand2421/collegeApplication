from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.AutoField(primary_key = True)
    department_name = models.CharField(max_length=250, blank=False)
    department_shor_name = models.CharField(max_length=250, blank=False)

    class Meta:
        ordering = ('department_name',)

    def __str__(self):
        return self.department_name

    def __unicode__(self):
        return self.department_name


class Student(models.Model):
    student_id = models.AutoField(max_length=11,null=False, primary_key = True)
    student_name = models.CharField(max_length=250, blank=False)
    student_email = models.EmailField(max_length=250)
    student_dob = models.DateField()
    department_id = models.ForeignKey(Department,on_delete= models.CASCADE)

    class Meta:
        ordering = ('student_id',)

    def __str__(self):
        return str(self.student_id)

    def __unicode__(self):
        return str(self.student_id)


class Subjects(models.Model):
    subject_id = models.AutoField(null=False, primary_key = True)
    subject_code = models.CharField(max_length=6, blank=False, default="Subject Code")
    subject_name = models.CharField(max_length=250, blank=False)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ('subject_code',)

    def __str__(self):
        return str('%s %s'%(self.subject_code,self.subject_name))

    def __unicode__(self):
        return str('%s %s' % (self.subject_code, self.subject_name))