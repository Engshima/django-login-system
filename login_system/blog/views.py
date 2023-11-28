from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.



def home(reguest):
      posts = Post.objects.all()
      
      context = {
            'posts': posts,
            'title': 'Zen of Python',
      }
      return render(reguest,'blog/home.html',context)
    

def about(reguest):
      return render(reguest,'blog/about.html')
    