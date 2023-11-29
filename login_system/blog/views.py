from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import PostForm
from django.shortcuts import get_object_or_404

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
      
      elif request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"the post has been created successfully")
                return redirect('blog:posts')
            else:
                  
                return render(request,'blog/post_form.html',{'form':form})
                messages.error(request, 'Please correct the following errors:')
          
           

def PostEdit(request,id):
      post = get_object_or_404(Post,id=id)
      if request.method=='GET':
            form = PostForm(instance=post)
            context = {
                  'form': form,
                  'id' :  id,
            }
            return render (request,'blog/post_form.html',context)
      
      elif request.method =='POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,"The post has been updated successfully.")
                return redirect('blog:posts')
                
            else:
                  messages.error(request,'Please correct the following errors:')
                  return render (request,'blog/post_form.html',{'form':form})
            
                  
          
     

     
def about(request):
      return render(request,'blog/about.html')
    