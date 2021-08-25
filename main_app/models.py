from django.db import models

class Dive(models.Model):
  number = models.IntegerField('Dive Number')
  location = models.CharField(max_length=100)
  max_depth = models.IntegerField()

  def __str__(self):
    return f"#{self.number}: {self.location}"

class Note(models.Model):
  note = models.TextField(max_length=250)
  dive = models.ForeignKey(Dive, on_delete=models.CASCADE)

  def __str__(self):
    return f"Note: {self.note}"