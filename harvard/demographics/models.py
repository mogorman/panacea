from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EnvironmentalExposure(models.Model):
    label = models.CharField(max_length=100)

class GeneticMutation(models.Model):
    label = models.CharField(max_length=100)

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True)
    siblings = models.IntegerField(blank=True)
    environmentals = models.ManyToManyField(EnvironmentalExposure)
    mutations = models.ManyToManyField(GeneticMutation)
    creator_id = models.OneToOneField(User)
    status =  models.IntegerField(default = 1) # 1 1 = not reviewd, 2 reviewed not accepted, 3 reviewed accepted

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=0) # 0 patient, 1 viewer, 2 editor
