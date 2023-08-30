from django.urls import path
<<<<<<< HEAD
from .views import postList, postDetail,PostCreateView,commentListView,projects_and_news,CommentUpdateView,PostUpdateView
=======
from .views import postList, postDetail,PostCreateView,commentListView,homeView,RecentPosts,CreatePost
>>>>>>> main

urlpatterns = [
    path("", postList.as_view(), name="post_list"),
    path("details/", postDetail, name="post_detail"),
    path("create/", CreatePost.as_view(), name="post_create"),
    path("comment/", commentListView.as_view(), name="comment_create"),
<<<<<<< HEAD
    path("home/", projects_and_news, name="home"),
    path('<int:post_id>/comments/update/<int:comment_id>/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post-update'),
=======
    path("home/", homeView, name="home"),
    path("recent/", RecentPosts.as_view(), name="comment_create"),



>>>>>>> main

]
