from django.urls import path
from .views import blogList, blogDetail

urlpatterns = [
    path("", blogList.as_view(), name="blog_list"),
    path("<int:pk>/", blogDetail.as_view(), name="blog_detail"),
]
