from django.contrib import admin

from .models import Patient, Profile, GeneticMutation, EnvironmentalExposure

admin.site.register(Patient)
admin.site.register(Profile)
admin.site.register(GeneticMutation)
admin.site.register(EnvironmentalExposure)
