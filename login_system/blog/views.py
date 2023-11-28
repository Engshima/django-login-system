from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PostForm

# Create your views here.



def home(request):
      posts = Post.objects.all()
      
      context = {
            'posts': posts,
            'title': 'Zen of Python',
      }
      return render(request,'blog/home.html',context)
    
def PostCreate(request):
      if request.method == 'GET':
            context = {'form': PostForm()}
            return render(request, 'blog/post_form.html', context)
      
      if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog:posts')
            else:
                  return render(request,'blog/post_form.html',{'form':form})

def about(request):
      return render(request,'blog/about.html')
    