from django.urls import path
from .views import postList, postDetail,commentListView,homeView,RecentPosts,CreatePost,CommentUpdateView,PostUpdateView,TestView

urlpatterns = [
    path("", postList, name="post_list"),
    path("details/", postDetail, name="post_detail"),
    path("create/", CreatePost.as_view(), name="post_create"),
    path("comment/", commentListView.as_view(), name="comment_create"),
    path('<int:post_id>/comments/update/<int:comment_id>/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post-update'),
    path("home/", homeView, name="home"),
    path("recent/", RecentPosts, name="comment_create"),
    path("test/", TestView.as_view(), name="test_create"),
]
