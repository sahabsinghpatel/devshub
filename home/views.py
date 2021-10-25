from django.shortcuts import render
from blog.models import BlogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def search(request):
    query=request.GET.get('query')
    posts_title=BlogPost.objects.all().filter(title__contains=query)
    posts_content=BlogPost.objects.all().filter(content__contains=query)
    postsss=(posts_title |posts_content).distinct()
    postss=Paginator(postsss, 1)
    page=request.GET.get('page')
    try:
        posts=postss.get_page(page)
    except PageNotAnInteger:
        posts=postss.page(1)
    except EmptyPage:
        posts=postss.page(postss.num_pages)
    return render(request, 'home/search.html', {'query':query, 'posts' : posts})
