from django.db import models
 
# Create your models here.
from django.db import models
 
# Create your models here.
class Createadmin(models.Model):
   username=models.CharField(max_length=30,null=True,blank=False)
   password=models.CharField(max_length=30,null=True,blank=False)
 
class Group(models.Model):
   group_id=models.CharField(max_length=30,null=True,blank=False)
   group_name=models.CharField(max_length=30,null=True,blank=False)
   def __str__(self):
       return self.group_name
 
class Location(models.Model):
   location_id=models.CharField(max_length=30,null=True,blank=False)
   location_name=models.CharField(max_length=30,null=True,blank=False)
   def __str__(self):
       return self.location_name
 
class Student(models.Model):
   studentname=models.CharField(max_length=30,null=True,blank=False)
   groupname=models.CharField(max_length=30,null=True,blank=False)
   locationname=models.CharField(max_length=30,null=True,blank=False)
   first_name=models.CharField(max_length=30,null=True,blank=False)
   last_name=models.CharField(max_length=30,null=True,blank=False)
   parent_name=models.CharField(max_length=30,null=True,blank=False)
   email=models.CharField(max_length=30,null=True,blank=False)
   remarks=models.CharField(max_length=30,null=True,blank=False)
   def __str__(self):
       return self.studentname
  
 
# class Index(models.Model):
#     group_name=models.CharField(max_length=30,null=True,blank=False)
#     location_name=models.CharField(max_length=30,null=True,blank=False)
#     student_name=models.CharField(max_length=30,null=True,blank=False)
  
 
 
 
 
 
 


 

 
 
 
 
 
 

