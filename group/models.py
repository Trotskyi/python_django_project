from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Group(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length = 200)
    chief = models.ForeignKey('student.Student', blank = True, null=True, on_delete=models.SET_NULL)



