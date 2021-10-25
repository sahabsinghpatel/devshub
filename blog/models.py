from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy
from django.db.models.fields import DateField, TextField, TimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    catagity=models.CharField(max_length=25)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail=models.ImageField(upload_to="blog/")
    desc=models.CharField(max_length=300)
    content=models.TextField()
    date=DateField(auto_now_add=True)
    time=TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering=['time']

# class BlogImg(models.Model):
#     post=ForeignKey(BlogPost)
#     images=ImageField(upload_to=f"/blog/{BlogPost.slug}/")

class Comment(models.Model):
    sno=models.AutoField(primary_key=True)
    post=ForeignKey(BlogPost, on_delete=CASCADE)
    commenter=ForeignKey(User, on_delete=CASCADE)
    parent=ForeignKey('self', default="", on_delete=CASCADE,  related_name="replyof", null=True)
    comment=TextField()
    time=TimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    class Meta:
        ordering=['-time']
