from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def add_comment_view(request):
    post = get_object_or_404(Post)
    if request.method == 'POST':
        form = CommentForm 
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else: 
        form = CommentForm()
    template = 'add_comment.html'
    return render(request, template)
 
