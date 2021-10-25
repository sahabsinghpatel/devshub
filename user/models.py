import PIL
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.related import ForeignKey
from PIL import Image

class Profile(models.Model):
    user=ForeignKey(User, on_delete=models.CASCADE)
    name=CharField(max_length=50, blank=True)
    email=EmailField(max_length=50, blank=True)
    pic=models.ImageField(upload_to='user/', blank=True)
    about=CharField(max_length=500)
    contact=CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.pic.path)
        width, height = img.size  
        if width > 300 and height > 300:
            img.thumbnail((width, height))
        if height < width:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
        elif width < height:
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))
        if width > 300 and height > 300:
            img.thumbnail((300, 300))
        img.save(self.pic.path)
