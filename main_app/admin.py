from django.contrib import admin
from .models import Dive, Note, Buddy, Photo

admin.site.register(Dive)
admin.site.register(Note)
admin.site.register(Buddy)
admin.site.register(Photo)