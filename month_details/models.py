from django.db import models

# Create your models here.
class MonthDetails(models.Model):
    monthnumber=models.IntegerField
    img=models.ImageField(upload_to='pics')
    monthname=models.CharField(max_length=20)
    desc=models.TextField()


