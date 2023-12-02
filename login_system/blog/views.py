from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.



def home(request):
      posts = Post.objects.all()
      
      context = {
            'posts': posts,
            'title': 'Zen of Python',
      }
      return render(request,'blog/home.html',context)


@login_required    
def PostCreate(request):
      if request.method == 'GET':
            context = {'form': PostForm()}
            return render(request, 'blog/post_form.html', context)
      
      elif request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.author=request.user
                user.save() 
                messages.success(request,"the post has been created successfully")
                return redirect('blog:posts')
            else:
                  
                return render(request,'blog/post_form.html',{'form':form})
                messages.error(request, 'Please correct the following errors:')
          
           
@login_required
def PostEdit(request,id):
      queryset=Post.objects.filter(author=request.user)
      post = get_object_or_404(queryset,id=id)
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
            
                  
@login_required          
def PostDelete(request,id):
      queryset=Post.objects.filter(author=request.user)
      post = get_object_or_404(queryset, pk=id)
      if request.method=='GET':
            form = PostForm(instance=post)
            context={
                  'form':form,
                  'id' : id,
            }
            return render(request, 'blog/post_delete.html',context)
      elif request.method=='POST':
            post.delete()
            messages.success(request,"'The post has been deleted successfully.'.")
            return redirect('blog:posts')
             

     
def about(request):
      return render(request,'blog/about.html')
    