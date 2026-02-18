from django.db import models

# Create your models here.
class user(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField()
    pwd=models.CharField(max_length=50)
    phno=models.IntegerField()
    class Meta:
        db_table="user" #Meta is used to copy the defined attributes already,db_table only works then
    
class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    pin=models.IntegerField()
    state=models.CharField(50)
    city = models.CharField(50)
    email = models.EmailField()
    pwd=models.CharField(50)
    phno=models.IntegerField()
    adhar = models.IntegerField()
    




'''
to apply any changes in models into database run

py manage.py makemigrations

py manage.py migrate'''