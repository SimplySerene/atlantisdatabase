from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Elective, Review

admin.site.register(Elective)
admin.site.register(Review)
