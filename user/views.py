from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login as login_user, logout as logout_user, authenticate
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
import os

@login_required(login_url='/user/login/')
def index(request):
    username=request.user.username
    user=User.objects.get(username=username)
    userd=Profile.objects.get(user=user)
    return render(request, 'user/index.html', {'userd':userd})

def signup(request):
    if request.user.is_authenticated:
        message=messages.warning(request, 'You Already Have an Account. No Need.')
        return redirect('/user/')
    else:
        if request.method=='POST':
            name=request.POST.get('name')
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            if len(name) < 3 or len(username) < 3 or len(password) < 3 or len(email) < 9:
                return redirect('/user/signup')
            else:
                user=User.objects.create_user(username,email, password)
                user.save()
                user_profile=Profile.objects.create(user=user, email=email, name=name)
                user_profile.save()
                login_user(request, user)
                return redirect('/user/')
        else:
            return render(request, 'user/signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/user/')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                return redirect('/')
            else:
                return redirect('/user/login')
        else:
            return render(request, 'user/login.html')

@login_required(login_url='/user/login')
def logout(request):
    logout_user(request)
    return redirect('/')

@login_required(login_url='/user/login/')
def editprofile(request):
    if request.method=='POST':
        name=request.POST.get('name')
        about=request.POST.get('about')
        contact=request.POST.get('contact')
        user=User.objects.get(username=request.user.username)
        userprofile=Profile.objects.get(user=user)
        userprofile.name=name
        userprofile.about=about
        userprofile.contact=contact
        userprofile.save()
        return redirect('/user/')
    else:
        username=request.user.username
        user=User.objects.get(username=username)
        profile=Profile.objects.get(user=user)
        return render(request, 'user/editprofile.html', {'profile':profile})

def changepass(request):
    if request.method=='POST':
        username=request.user.username
        pass_now=request.POST.get('passwordnow')
        pass_new=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        user=authenticate(username=username, password=pass_now)
        if user is not None:
            user=User.objects.get(username=username)
            user.set_password(pass_new)
            user.save()
            login_user(request, user)
            return redirect('/user/')
        else:
            return redirect('/user/changepass/')
    else:
        return render(request, 'user/changepass.html')

def userprofile(request, user):
    user=User.objects.get(username=user)
    author=Profile.objects.get(user=user)
    posts=BlogPost.objects.filter(author=user).first()
    return render(request, 'user/userprofile.html', {'author':author, 'posts':posts})

@login_required(login_url='/user/login/')
def addPost(request):
    if request.method=="POST":
        username=request.user.username
        author=User.objects.get(username=username)
        title=request.POST.get('title')
        thumbnail=request.FILES['thumbnail']
        slug=request.POST.get('slug')
        catagiry=request.POST.get('catagiry')
        desc=request.POST.get('desc')
        content=request.POST.get('content')
        post=BlogPost.objects.create(author=author, title=title, thumbnail=thumbnail, slug=slug, catagity=catagiry, desc=desc, content=content)
        post.save()
        return redirect(f'/blog/{username}/')
    else:
        return render(request, 'user/addPost.html')

def editPic(request):
    if request.method=='POST':
        username=request.user.username
        user=User.objects.get(username=username)
        profile=Profile.objects.get(user=user)
        pic=request.FILES.get('profile-pic')
        try:
            current_pic=profile.pic.path
            if current_pic is not None:
                os.remove(current_pic)
        except Exception as e:
            pass
        profile.pic=pic
        profile.save()
        return redirect("/user/")
    else:
        return redirect("/user/")
