from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required
def dives_index(request):
    dives = Dive.objects.filter(user=request.user)
    return render(request, 'dives/index.html', {'dives': dives})


@login_required
def dives_detail(request, dive_id):
    dive = Dive.objects.get(id=dive_id)
    buddies_not_currently_attending = Buddy.objects.exclude(
        id__in=dive.buddies.all().values_list('id'))
    note_form = NoteForm()
    return render(request, 'dives/detail.html', {
        'dive': dive, 'note_form': note_form, 'buddies_not_currently_attending': buddies_not_currently_attending
    })


class DiveCreate(LoginRequiredMixin, CreateView):
    model = Dive
    fields = ['number', 'location', 'max_depth']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DiveUpdate(LoginRequiredMixin, UpdateView):
    model = Dive
    fields = ['location', 'max_depth']


class DiveDelete(LoginRequiredMixin, DeleteView):
    model = Dive
    success_url = '/dives/'


@login_required
def add_note(request, dive_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.dive_id = dive_id
        new_note.save()
    return redirect('dives_detail', dive_id=dive_id)


class BuddyCreate(LoginRequiredMixin, CreateView):
    model = Buddy
    fields = ['name', 'color']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BuddyList(LoginRequiredMixin, ListView):
    model = Buddy


class BuddyDetail(LoginRequiredMixin, DetailView):
    model = Buddy


class BuddyUpdate(LoginRequiredMixin, UpdateView):
    model = Buddy
    fields = ['name', 'color']


class BuddyDelete(LoginRequiredMixin, DeleteView):
    model = Buddy
    success_url = '/buddies/'


@login_required
def associate_buddy_with_dive(request, dive_id, buddy_id):
    Dive.objects.get(id=dive_id).buddies.add(buddy_id)
    return redirect('dives_detail', dive_id=dive_id)


@login_required
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


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dives_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
