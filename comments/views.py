from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Comment
from django import forms
from django.utils import timezone
from .forms import CommentForm




def index(request):
  latest_comment_list = Comment.objects.order_by('-comment_date')[:10]
  context = {'latest_comment_list': latest_comment_list}
  return render(request, 'comments/index.html', context)

def detail(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)
  return render(request, 'comments/detail.html', {'comment': comment})

def new(request):
  return render(request, 'comments/new.html')

def create(request):
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.comment_date = timezone.now()
      comment.sender_ip = Comment.get_client_ip(comment,request)
      comment.save()
      return redirect('/comments/')
  else:
    form = CommentForm()
  return render(request, 'comments/form.html', {'form': form})

def edit(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)
  if request.method == "POST":
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.comment_date = timezone.now()
      comment.sender_ip = Comment.get_client_ip(comment,request)
      comment.save()
      return render(request, 'comments/detail.html', {'comment': comment})
  else:
    form = CommentForm(instance=comment)
  return render(request, 'comments/form.html', {'form': form,'comment': comment})
  
