from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='user'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('edit-pic/', views.editPic, name='editpic'),
    path('changepass/', views.changepass, name='changepass'),
    path('add-post/', views.addPost, name='addPost'),
    path('<str:user>/', views.userprofile, name='userprofile'),
]
