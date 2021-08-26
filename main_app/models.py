from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Buddy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('buddies_detail', kwargs={'pk': self.id})


class Dive(models.Model):
    number = models.IntegerField('#')
    date = models.DateField()
    site = models.CharField(max_length=100)
    max_depth = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buddies = models.ManyToManyField(Buddy)

    def __str__(self):
        return f"#{self.number}: {self.location}"

    def get_absolute_url(self):
        return reverse('dives_detail', kwargs={'dive_id': self.id})

    class Meta:
        ordering = ['-number']


class Note(models.Model):
    note = models.TextField(max_length=250)
    dive = models.ForeignKey(Dive, on_delete=models.CASCADE)

    def __str__(self):
        return f"Note: {self.note}"

    # class Meta:
        # ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=250)
    dive = models.OneToOneField(Dive, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for dive_id: {self.dive_id} @{self.url}"


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Trip: {self.destination}, {self.country}_{self.start_date} - {self.end_date}"

    def get_absolute_url(self):
        return reverse('trips_detail', kwargs={'trip_id': self.id})

    class Meta:
        ordering = ['-start_date']
