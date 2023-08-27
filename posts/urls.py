from django.urls import path
from .views import postList, postDetail

urlpatterns = [
    path("", postList.as_view(), name="post_list"),
    path("<int:pk>", postDetail.as_view(), name="post_detail"),
]
