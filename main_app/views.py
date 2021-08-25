from django.shortcuts import render
from .models import Dive

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dives_index(request):
  dives = Dive.objects.all()
  return render(request, 'dives/index.html', { 'dives': dives })

def dives_detail(request, dive_id):
  dive = Dive.objects.get(id=dive_id)
  return render(request, 'dives/detail.html', { 'dive': dive })