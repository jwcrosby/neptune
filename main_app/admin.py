from django.contrib import admin
from .models import Dive, Photo, Note, Buddy, Trip

admin.site.register(Dive)
admin.site.register(Photo)
admin.site.register(Note)
admin.site.register(Buddy)
admin.site.register(Trip)