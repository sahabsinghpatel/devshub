from django.urls import path

from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='blog'),
    path('post-comment', views.postcomment, name='post-comment'),
    path('<str:author>/', views.author, name='author'),
    path('<str:author>/<str:slug>/', views.post, name='post'),
]
