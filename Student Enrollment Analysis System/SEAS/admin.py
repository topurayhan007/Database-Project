from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.
admin.site, register(School)
admin.site, register(Department)
admin.site, register(Faculty)
admin.site, register(Course)
admin.site, register(Classroom)
admin.site, register(Section)