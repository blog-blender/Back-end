from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from blogs.models import blog

class Post(models.Model):
    title = models.CharField(max_length=256)
    Auther_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(default="", null=True, blank=True)
    blog_id = models.ForeignKey(blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Like(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    content=models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.content

class Photo(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    data=models.ImageField(upload_to='post_picture/', blank=True, null=True)


class test(models.Model):
    photo_data = models.ImageField(upload_to='post_picture/')
