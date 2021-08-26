from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Dive, Buddy, Photo
from .forms import NoteForm
import boto3
import uuid

S3_BASE_URL = "https://s3.us-west-1.amazonaws.com/"
BUCKET = 'neptune-jwc'


class Home(LoginView):
    template_name = 'home.html'


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
    fields = ['number', 'location', 'max_depth']


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


def add_photo(request, dive_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
        # uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
        key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to dive_id or dive (if you have a dive object)
            photo = Photo(url=url, dive_id=dive_id)
            # Remove old photo if it exists
            dive_photo = Photo.objects.filter(dive_id=dive_id)
            if dive_photo.first():
                dive_photo.first().delete()
            photo.save()
        except Exception as err:
            print('An error occurred uploading file to S3: %s' % err)
    return redirect('dives_detail', dive_id=dive_id)
