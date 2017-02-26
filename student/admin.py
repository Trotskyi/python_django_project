from django.contrib import admin
from models import Student
# Register your models here.

class StudAdmin(admin.ModelAdmin):
    search_fields = ('surname', 'name', 'student_card')

admin.site.register(Student, StudAdmin)