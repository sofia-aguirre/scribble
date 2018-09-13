from django.shortcuts import render, redirect
from .models import Post, Comment
# import forms here

##########
# Posts view functions
##########

def post_list(request): 
    # getting all posts
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # getting one post by id (pk)
    posts = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'posts': posts})

##########
# Comments view functions
##########

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', {'comments': comments})