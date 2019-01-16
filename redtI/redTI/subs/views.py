from .models import Subrediti, Thread, Post
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.views import generic
# Create your views here.
class SubreditisView(generic.ListView):
    template_name = 'subs/subreditis.html'
    model = Subrediti
    context_object_name = 'subreditis'

class SubreditiView(generic.DetailView):
    template_name = 'subs/subrediti.html'
    model = Subrediti

class ThreadView(generic.DetailView):
    template_name = 'subs/thread.html'
    model = Thread

class PostView(generic.DetailView):
    template_name = 'subs/post.html'
    model = Post