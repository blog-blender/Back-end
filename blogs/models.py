from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class blog(models.Model):

    title = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    banner = models.ImageField(upload_to='blog_banner/', blank=True, null=True)
    blog_pic = models.ImageField(upload_to='blog_pic/', blank=True, null=True)
    description = models.TextField(default="", null=True, blank=True)
    categories = models.JSONField(default=list, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

