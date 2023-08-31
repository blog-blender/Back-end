from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class blog(models.Model):
    title = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    banner = models.ImageField(upload_to='blog_banner/', blank=True, null=True)
    blog_pic = models.ImageField(upload_to='blog_pic/', blank=True, null=True)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

class Follower(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    blog_id = models.ForeignKey(blog, on_delete=models.CASCADE, null=True, blank=True)


class Categories(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)


class Category_associate(models.Model):
    category_name = models.ForeignKey(Categories,max_length=100 , on_delete=models.CASCADE)
    blog_id = models.ForeignKey(blog,max_length=100 , on_delete=models.CASCADE)



