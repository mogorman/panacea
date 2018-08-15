from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Patient, Profile
from .forms import SignUpForm

# Create your views here.
@login_required
def index(request):
    username = None
    profile = None
    if request.user.is_authenticated():
        profile = request.user.profile
        username = request.user.username
    template = loader.get_template('demos/index.html')
    return HttpResponse(template.render({'username': username, 'profile': profile}, request))

@login_required
def add(request):
    return HttpResponse("Hello you are at the demographics add.")

@login_required
def edit(request, patient_id):
    return HttpResponse("Hello you are at the demographics add. {}".format(patient_id))

@login_required
def list(request):
    patients = Patient.objects.all()
    return HttpResponse("Hello you are at the demographics list. {}".format([patient.first_name for patient in patients]))

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
            print("wtf mate {}".format(user.profile.id))
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/demo/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
