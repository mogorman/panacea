from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class EnvironmentalExposure(models.Model):
    label = models.CharField(max_length=100)

class GeneticMutation(models.Model):
    label = models.CharField(max_length=100)

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    siblings = models.IntegerField(blank=True, null=True)
    environmentals = models.ManyToManyField(EnvironmentalExposure, blank=True, null=True)
    mutations = models.ManyToManyField(GeneticMutation, blank=True, null=True)
    creator_id = models.OneToOneField(User)
    status =  models.IntegerField(default = 1) # 1 1 = not reviewd, 2 reviewed not accepted, 3 reviewed accepted
    deleted = models.IntegerField(blank=True, null=True) # support levels of soft deleting

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=0) # 0 patient, 1 viewer, 2 editor

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
