from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, EnvironmentalExposure, GeneticMutation
from django.db.utils import OperationalError

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class PatientForm(forms.ModelForm):
    # catch error when db doesnt exist
    try:
        environmentals = forms.MultipleChoiceField(choices=[(choice.pk, choice.label) for choice in EnvironmentalExposure.objects.all().filter(deleted=None)], widget=forms.CheckboxSelectMultiple, required=False)
        mutations = forms.MultipleChoiceField(choices=[(choice.pk, choice.label) for choice in GeneticMutation.objects.all().filter(deleted=None)], widget=forms.CheckboxSelectMultiple, required=False)
    except OperationalError:
        pass
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'age', 'siblings', )

class PatientFormComplete(forms.ModelForm):
    try:
        environmentals = forms.MultipleChoiceField(choices=[(choice.pk, choice.label) for choice in EnvironmentalExposure.objects.all().filter(deleted=None)], widget=forms.CheckboxSelectMultiple, required=False)
        mutations = forms.MultipleChoiceField(choices=[(choice.pk, choice.label) for choice in GeneticMutation.objects.all().filter(deleted=None)], widget=forms.CheckboxSelectMultiple, required=False)
    except OperationalError:
        pass
    class Meta:
        model = Patient
#        fields = ('first_name', 'last_name', 'age', 'siblings', )
        fields = '__all__'
