from django.contrib import admin
from .models import blog,Follower,Category_associate,Categories

# Register your models here.
admin.site.register(blog)
admin.site.register(Follower)
admin.site.register(Category_associate)
admin.site.register(Categories)
