from django.db import models

from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from django.contrib.auth import authenticate

class AppUserManager(BaseUserManager):
    def create_user(self,email,phonenumber=None,firstname=None,lastname=None,username=None, password=None,date_of_birth=None):
        if not email:
            raise ValueError('User should have email address')
        user = self.model(
            email = self.normalize_email(email),
            phonenumber = phonenumber,
            first_name = firstname,
            last_name = lastname,
            username = username,
            date_of_birth = date_of_birth,
            is_active = True,
            is_admin = False
        )
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self,email,phonenumber=None,firstname=None,lastname=None,username=None, password=None,data_of_birth=None):
        user = self.model(
            email=self.normalize_email(email),
            phonenumber=phonenumber,
            first_name=firstname,
            last_name=lastname,
            username=username,
            password = password,
            data_of_birth = data_of_birth,
            is_active = True
        )
        user.is_admin = True
        user.save(using = self._db)
        return user




class AppUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=250, unique=True)
    user_id = models.AutoField(primary_key = True, blank=False)
    phonenumber = models.CharField(max_length=12, blank=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank= False)
    date_of_birth = models.DateField()
    is_active = models.BooleanField()
    is_admin = models.BooleanField()

    objects = AppUserManager()

    USERNAME_FIELD = "email"


    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin