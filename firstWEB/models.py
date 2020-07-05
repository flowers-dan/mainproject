from __future__ import unicode_literals
from django.db import models
#create your models here.
class cal(models.Model):
    value_a=models.CharField(max_length=10)
    value_b=models.FloatField(max_length=10)
    result=models.CharField(max_length=10)
#json
class student(models.Model):
    s_id=models.CharField(max_length=10)
    s_name=models.CharField(max_length=150)
    s_birth=models.CharField(max_length=150)

