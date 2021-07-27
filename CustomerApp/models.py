from django.db import models

# Create your models here.
class Customer(models.Model):
    cname=models.CharField(max_length=10)
    cid=models.IntegerField()
    bal=models.FloatField()
    dob=models.DateField()
    email=models.EmailField()
    phoneno=models.IntegerField()
    address=models.TextField()
