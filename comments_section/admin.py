from django.contrib import admin
from .models import Post, Comment
 
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

admin.site.register(Comment, CommentAdmin)
