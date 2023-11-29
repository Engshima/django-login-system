from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.

def sign_in(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('blog:posts')
        form=LoginForm()
        context={
            'form': form
        }
        return render(request,'users/login.html',context)
    
    elif request.method=='POST':
        
        form = LoginForm(request.POST)
       
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                # User is authenticated
                login(request,user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('blog:posts')
        # form is not valid or user is not authenticated
        
        messages.error(request,f'Invalid username or password')   
        return render(request,'users/login.html',{'form':form})     
           
        
def sign_out(request):
   logout(request)
   messages.success(request,f'You have been logged out.')  
   return redirect('users:login')
                       
        
