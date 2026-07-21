from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class Trip(models.Model):
    name=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    created_by=ForeignKey(User,on_delete=models.CASCADE)

class Member(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    join_date=models.DateField()

class Activity(models.Model):
    trip=models.ForeignKey(Trip,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    location=models.CharField(max_length=200)



