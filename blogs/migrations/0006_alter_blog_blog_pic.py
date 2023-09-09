# Generated by Django 4.1.5 on 2023-09-09 12:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]