from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    class Meta:
        ordering = ['group_name', 'surname']

    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 50)
    father = models.CharField(max_length = 50)
    birthday = models.DateField()
    student_card = models.CharField(max_length = 20)
    group_name = models.ForeignKey('group.Group', blank = True, related_name='students')

    class Meta:
        ordering = ['group_name', 'surname']

    def get_name(self):
        return "%s %s %s" % (self.surname, self.name, self.father)

    @models.permalink
    def get_edit_url(self):
        return  'edit_student', (self.pk, )

    @models.permalink
    def get_delete_url(self):
        return 'delete_student', (self.pk, )