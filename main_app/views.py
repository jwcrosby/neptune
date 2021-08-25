from django.shortcuts import render

from django.http import HttpResponse

class Dive: 
  def __init__(self, number, location, max_depth, notes):
    self.number = number
    self.location = location
    self.max_depth = max_depth
    self.notes = notes

dives = [
  Dive(1, 'Key Largo', 25, "Pretty not bad"),
  Dive(4, 'Cozumel', 20, "Pretty not bad"),
  Dive(25, 'Denver', 50, "Pretty not bad"),
  Dive(66, 'Pawleys Island', 123, "Pretty not bad")
]


def home(request):
  return HttpResponse('<h1>neptune</h1>')

def about(request):
  return render(request, 'about.html')

def dives_index(request):
  return render(request, 'dives/index.html', { 'dives': dives })