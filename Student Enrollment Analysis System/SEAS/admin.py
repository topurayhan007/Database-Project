from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.
admin.site, register(School_T)
admin.site, register(Department_T)
admin.site, register(Faculty_T)
admin.site, register(Course_T)
admin.site, register(Classroom_T)
admin.site, register(Section_T)