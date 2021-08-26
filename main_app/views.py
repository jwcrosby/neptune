from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dive, Buddy
from .forms import NoteForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dives_index(request):
    dives = Dive.objects.all()
    return render(request, 'dives/index.html', {'dives': dives})


def dives_detail(request, dive_id):
    dive = Dive.objects.get(id=dive_id)
    buddies_not_currently_attending = Buddy.objects.exclude(
        id__in=dive.buddies.all().values_list('id'))
    note_form = NoteForm()
    return render(request, 'dives/detail.html', {
        'dive': dive, 'note_form': note_form, 'buddies_not_currently_attending': buddies_not_currently_attending
    })


class DiveCreate(CreateView):
    model = Dive
    fields = ['number', 'location', 'max depth']


class DiveUpdate(UpdateView):
    model = Dive
    fields = ['location', 'max_depth']


class DiveDelete(DeleteView):
    model = Dive
    success_url = '/dives/'


def add_note(request, dive_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.dive_id = dive_id
        new_note.save()
    return redirect('dives_detail', dive_id=dive_id)


class BuddyCreate(CreateView):
    model = Buddy
    fields = '__all__'


class BuddyList(ListView):
    model = Buddy


class BuddyDetail(DetailView):
    model = Buddy


class BuddyUpdate(UpdateView):
    model = Buddy
    fields = ['name', 'color']


class BuddyDelete(DeleteView):
    model = Buddy
    success_url = '/buddies/'


def associate_buddy_with_dive(request, dive_id, buddy_id):
    Dive.objects.get(id=dive_id).buddies.add(buddy_id)
    return redirect('dives_detail', dive_id=dive_id)
