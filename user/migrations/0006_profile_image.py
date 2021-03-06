# Generated by Django 3.2.8 on 2021-10-25 07:06

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=image_cropping.fields.ImageRatioField('pic', '400x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image'),
        ),
    ]
