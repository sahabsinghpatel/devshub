import json
from django.db.models import fields
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import blog
from .models import BlogPost, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    postsss=BlogPost.objects.all().order_by('time')
    postss=Paginator(postsss, 1)
    page=request.GET.get('page', 1)
    try:
        posts=postss.get_page(page)
    except PageNotAnInteger:
        posts=postss.page(1)
    except EmptyPage:
        posts=postss.page(postss.num_pages)
    return render(request, 'blog/index.html', {"posts": posts})

def author(request, author):
    author=User.objects.get(username=author)
    postsss=BlogPost.objects.filter(author=author).order_by('time')
    postss=Paginator(postsss, 1)
    page=request.GET.get('page')
    try:
        posts=postss.get_page(page)
    except PageNotAnInteger:
        posts=postss.page(1)
    except EmptyPage:
        posts=postss.page(postss.num_pages)
    return render(request, 'blog/author.html', {'posts':posts, 'author':author})

def post(request, author, slug):
    post=BlogPost.objects.get(slug=slug)
    comments=Comment.objects.all().filter(post=post, parent=None).order_by('-time')
    replies=Comment.objects.all().filter(post=post).exclude(parent=None).order_by('-time')
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    return render(request, 'blog/post.html', {'post' : post, 'comments':comments, 'replyDict':replyDict})

def postcomment(request):
    if request.method=='POST':
        commenter=request.user
        comment=request.POST.get('comment')
        post_id=request.POST.get('post')
        parent_id=request.POST.get('parent')
        post=BlogPost.objects.get(sno=post_id)
        if parent_id=="":
            Comment.objects.create(post=post, commenter=commenter, comment=comment)
        else:
            parent=Comment.objects.get(sno=parent_id)
            Comment.objects.create(post=post, commenter=commenter, comment=comment, parent=parent)
    return redirect(f'/blog/{post.author}/{post.slug}')
