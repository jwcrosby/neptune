from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

BUDDYICONS = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C')
)

AIRCHOICES = (
    ('A', 'Air'),
    ('N', 'Nitrox')
)

WEIGHTRATINGS = (
    ('E', '✔️'),
    ('P', '➕'),
    ('N', '➖')
)

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    start_date = models.DateField('Start Date', blank=True)
    end_date = models.DateField('End Date', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Trip: {self.destination}, {self.country}_{self.start_date} - {self.end_date}"

    def get_absolute_url(self):
        return reverse('trips_detail', kwargs={'trip_id': self.id})

    class Meta:
        ordering = ['-start_date']


class Buddy(models.Model):
    name = models.CharField(max_length=50, blank=True)
    icon = models.CharField(
        'Icon',
        max_length=1,
        choices=BUDDYICONS,
        # default=BUDDYICONS[0][0],
        blank=True,
        null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('buddies_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class Dive(models.Model):
    number = models.IntegerField('Dive #')
    date = models.DateField(blank=True, null=True)
    site = models.CharField('Dive Site', max_length=100, blank=True, null=True) 
    air_start = models.IntegerField('Air Start (psi)', blank=True, null=True)
    air_end = models.IntegerField('Air End (psi)', blank=True, null=True)
    air_choice = models.CharField(
        'Air Choice',
        max_length=1,
        choices=AIRCHOICES,
        # default=AIRCHOICES[0][0],
        blank=True,
        null=True
    )
    depth_avg = models.IntegerField('Average Depth (ft)', blank=True, null=True)
    depth_max = models.IntegerField('Max Depth (ft)', blank=True, null=True)
    bottom_time = models.IntegerField('Bottom Time (min)', blank=True, null=True)
    acc_bottom_time = models.IntegerField('Acc. Bottom Time (min)', blank=True, null=True)
    safety_stop_depth = models.IntegerField('Safety Stop Depth (ft)', blank=True, null=True)
    safety_stop_time = models.IntegerField('Safety Stop Time (min)', blank=True, null=True)
    temperature_air = models.IntegerField('Air Temperature (F)', blank=True, null=True)
    temperature_surface = models.IntegerField('Surface Temperature (F)', blank=True, null=True)
    temperature_bottom = models.IntegerField('Bottom Temperature (F)', blank=True, null=True)
    visibility = models.IntegerField('Visbility (ft)', blank=True, null=True)
    weather = models.CharField('Weather', max_length=100, blank=True, null=True) 
    suit_desc = models.CharField('Suit Description', max_length=100, blank=True, null=True) 
    suit_thickness = models.IntegerField('Thickness (mm)', blank=True, null=True)
    suit_notes = models.CharField('Additional Suit Notes', max_length=250, blank=True, null=True)
    weight = models.IntegerField('Weight (lb)', blank=True, null=True)
    weight_rating = models.CharField(
        'Weight Rating',
        max_length=1,
        choices=WEIGHTRATINGS,
        # default=WEIGHTRATINGS[0][0],
        blank=True,
        null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, blank=True, null=True, on_delete=models.SET_NULL)
    buddies = models.ManyToManyField(Buddy, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"#{self.number}: {self.site}"

    def get_absolute_url(self):
        return reverse('dives_detail', kwargs={'dive_id': self.id})

    class Meta:
        ordering = ['-number']


class Note(models.Model):
    note = models.CharField(max_length=250)
    dive = models.ForeignKey(Dive, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Note: {self.note}"

    class Meta:
        ordering = ['-created_date']


class Photo(models.Model):
    url = models.CharField(max_length=250)
    dive = models.OneToOneField(Dive, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Photo for dive_id: {self.dive_id} @{self.url}"
