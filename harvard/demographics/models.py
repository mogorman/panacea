from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class EnvironmentalExposure(models.Model):
    label = models.CharField(max_length=100)
    deleted = models.IntegerField(blank=True, null=True) # support levels of soft deleting

class GeneticMutation(models.Model):
    label = models.CharField(max_length=100)
    deleted = models.IntegerField(blank=True, null=True) # support levels of soft deleting

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    siblings = models.IntegerField(blank=True, null=True)
    environmentals = models.ManyToManyField(EnvironmentalExposure, blank=True, null=True, related_name="environmentals")
    mutations = models.ManyToManyField(GeneticMutation, blank=True, null=True, related_name="mutations")
    patient = models.ForeignKey(User, related_name="patient", blank=True, null=True) # if we are tying this patient record directly to a user record so 0 level profile user can see it
    creator = models.ForeignKey(User, related_name="creator")
    status =  models.IntegerField(default = 1) # 1 1 = not reviewed, 2 reviewed not accepted, 3 reviewed accepted
    deleted = models.IntegerField(blank=True, null=True) # support levels of soft deleting

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=0) # 0 patient, 1 viewer, 2 editor

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        # when a user is created create a patient level profile
        Profile.objects.create(user=instance)
        # also create a blank demographic to go along with it.
        Patient.objects.create(patient=instance, creator=instance)

    instance.profile.save()
