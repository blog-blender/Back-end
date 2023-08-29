from django.urls import path
from .views import postList, postDetail,PostCreateView,commentListView,homeView

urlpatterns = [
    path("", postList.as_view(), name="post_list"),
    path("details/", postDetail, name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("comment/", commentListView.as_view(), name="comment_create"),
    path("home/", homeView, name="home"),



]
