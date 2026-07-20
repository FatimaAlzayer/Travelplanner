from django.db import models

class Trip(models.Model):
    name=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    created_by=models.CharField(max_length=200)
