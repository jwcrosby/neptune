from django.db import models

class Dive(models.Model):
  number = models.IntegerField()
  location = models.CharField(max_length=100)
  max_depth = models.IntegerField()
  notes = models.TextField(max_length=250)

  def __str__(self):
    return f"#{self.note}: {self.location}"

class Note(models.Model):
  note = models.TextField(max_length=250)

  def __str__(self):
    return f"Note: {self.note}"