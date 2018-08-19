from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import extra_views
from django.contrib.auth.models import User

from .models import Patient, Profile
from .forms import SignUpForm, PatientForm, PatientFormComplete

# Create your views here.
@login_required
def index(request):
    profile = None
    if request.user.is_authenticated():
        profile = request.user.profile
    template = loader.get_template('demos/index.html')
    return HttpResponse(template.render({'user': request.user, 'profile': profile}, request))


@login_required
def add(request):
    user = User.objects.get(pk=request.user.id)
    patient = Patient.objects.create(patient=None, creator=user, deleted=1)
    return redirect('/demo/edit/{}'.format(patient.id))


@login_required
def edit_by_id(request, patient_id):
    # should check to see that a patient record exists here but it is required on creation so shouldnt be a problem
    instance = Patient.objects.get(pk=patient_id)
    instance.deleted = None
    if not instance:
        return redirect('/demo/')
    if request.method == 'POST':
        form = PatientFormComplete(request.POST, instance=instance)
        if form.is_valid():
            patient = form.save()
            patient.refresh_from_db()
            return redirect('/demo/list')
    else:
        form = PatientFormComplete(instance=instance)
    return render(request, 'demos/patient.html', {'form': form})


@login_required
def edit_by_patient(request, patient_id):
    # should check to see that a patient record exists here but it is required on creation so shouldnt be a problem
    instance = Patient.objects.get(patient=patient_id)
    if not instance:
        return redirect('/demo/')
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=instance)
        if form.is_valid():
            patient = form.save()
            patient.refresh_from_db()
            return redirect('/demo/')
    else:
        form = PatientForm(instance=instance)
    return render(request, 'demos/patient.html', {'form': form})


@login_required
def list(request):
    print("getting caught here")
    level = request.user.profile.level
    if level == 0:
        return redirect('/demo/')

    editable = False
    if level == 2:
        editable = True
    patients = Patient.objects.all().filter(deleted=None)
    return render(request, 'demos/patients.html', {'patients': patients, 'editable': editable})


@login_required
def status_update(request, patient_id, status):
    level = request.user.profile.level
    #if users doesnt have permissions to modify status redirect them
    if level != 2:
        return redirect('/demo/')
    patient = Patient.objects.get(pk=patient_id)

    if patient and (status == "1" or status == "2" or status == "3"):
        patient.status = status
        patient.save()
    return HttpResponse('OK')


@login_required
def review(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    return HttpResponse("Currently reviewing {}. {}".format(patient_id, patient.first_name))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.level = 0
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/demo/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
