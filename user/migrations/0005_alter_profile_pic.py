# Generated by Django 3.2.8 on 2021-10-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, upload_to='user/'),
        ),
    ]
