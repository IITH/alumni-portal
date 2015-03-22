from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Department(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Degree(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.short_name 

class UserInfo(models.Model):
    user = models.ForeignKey(User,unique=True)
    status = models.IntegerField(default=0) #-1:invalid email id, 0: first time user, 1, user updated the information once
    department = models.ForeignKey(Department,null=True,blank=True)
    degree = models.ForeignKey(Degree,null=True,blank=True)
    roll_no = models.CharField(max_length=10,null=True,blank=True)
    year_of_admission = models.IntegerField(null=True,blank=True)
    stream = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(max_length=20,null=True,blank=True)
    personal_email = models.EmailField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    def __unicode__(self):
        return self.department.code +' '+str(self.year_of_admission)+self.degree.code + self.roll_no



class SampleUser(models.Model):
    username = models.CharField(max_length=255)
    # TODO(rushiagr): password not secret. Make it
    password = models.CharField(max_length=255)
