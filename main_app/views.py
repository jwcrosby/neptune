from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dive
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
    note_form = NoteForm()
    return render(request, 'dives/detail.html', {
        'dive': dive, 'note_form': note_form
    })


class DiveCreate(CreateView):
    model = Dive
    fields = '__all__'


class DiveUpdate(UpdateView):
    model = Dive
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['location', 'max_depth']


class DiveDelete(DeleteView):
    model = Dive
    success_url = '/dives/'


def add_note(request, dive_id):
    form = NoteForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_note = form.save(commit=False)
        new_note.dive_id = dive_id
        new_note.save()
    return redirect('dives_detail', dive_id=dive_id)
