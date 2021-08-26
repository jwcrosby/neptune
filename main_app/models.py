from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    start_date = models.DateField('Start Date', blank=True)
    end_date = models.DateField('End Date', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"Trip: {self.destination}, {self.country}_{self.start_date} - {self.end_date}"

    def get_absolute_url(self):
        return reverse('trips_detail', kwargs={'trip_id': self.id})

    class Meta:
        ordering = ['-start_date']


class Buddy(models.Model):
    name = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=20, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('buddies_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class Dive(models.Model):
    number = models.IntegerField('#')
    date = models.DateField(blank=True)
    site = models.CharField(max_length=100, blank=True)
    max_depth = models.IntegerField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, blank=True, null=True, on_delete=models.SET_NULL)
    buddies = models.ManyToManyField(Buddy, blank=True)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"#{self.number}: {self.site}"

    def get_absolute_url(self):
        return reverse('dives_detail', kwargs={'dive_id': self.id})

    class Meta:
        ordering = ['-number']


class Note(models.Model):
    note = models.TextField(max_length=250)
    dive = models.ForeignKey(Dive, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"Note: {self.note}"

    class Meta:
        ordering = ['-created_date']


class Photo(models.Model):
    url = models.CharField(max_length=250)
    dive = models.OneToOneField(Dive, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"Photo for dive_id: {self.dive_id} @{self.url}"
