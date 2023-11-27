from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(reguest):
      return HttpResponse('<h1>home</h1>')
    

def about(reguest):
      return HttpResponse('<h1>about</h1>')
    