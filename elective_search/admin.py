from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Elective, Review


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewerName', 'elective', 'published']
    actions = [make_published]

admin.site.register(Elective)
admin.site.register(Review, ReviewAdmin)

