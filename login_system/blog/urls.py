from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    
    path('',views.home, name='posts'),
    path('about/',views.about, name='about'),
    path('post/create',views.PostCreate, name='PostCreate'),
    path('post/edit/<int:id>/',views.PostEdit, name='post-edit'),
    path('post/delete/<int:id>/',views.PostDelete, name='post-delete'),
]

