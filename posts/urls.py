from django.urls import path
from .views import postList, postDetail,PostCreateView,commentListView

urlpatterns = [
    path("", postList.as_view(), name="post_list"),
    path("<int:pk>", postDetail.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("comment/", commentListView.as_view(), name="comment_create"),

]



