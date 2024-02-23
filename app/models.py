from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    salary = models.IntegerField()
    date_of_joining = models.DateField()