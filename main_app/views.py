from django.shortcuts import render
from .models import Dive

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dives_index(request):
  dives = Dive.objects.all()
  return render(request, 'dives/index.html', { 'dives': dives })