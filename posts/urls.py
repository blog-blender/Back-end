from django.urls import path
from .views import postList, postDetail,commentListView,homeView,RecentPosts,CreatePost,CommentUpdateView,commentCreateView,UpdatePost,CreateLike,DeleteLike

urlpatterns = [
    path("", postList, name="post_list"),
    path("details/", postDetail, name="post_detail"),
    path("create/", CreatePost, name="post_create"),
    path("comment/", commentListView.as_view(), name="comment_list"),
    path("comment/create", commentCreateView.as_view(), name="comment_create"),
    path('comments/update/<int:comment_id>/', CommentUpdateView.as_view(), name='comment-update'),
    path('update/',UpdatePost, name='post-update'),
    path("home/", homeView, name="home"),
    path("recent/", RecentPosts, name="comment_create"),
    path("like/",CreateLike.as_view(),name="create_like"),
    path("like/delete/<int:like_id>",DeleteLike.as_view(),name="create_like")
]
