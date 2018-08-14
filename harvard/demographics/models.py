from django.db import models

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
