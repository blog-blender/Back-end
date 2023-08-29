from django.urls import path
from .views import postList, postDetail,PostCreateView,commentListView,projects_and_news,CommentUpdateView,PostUpdateView

urlpatterns = [
    path("", postList.as_view(), name="post_list"),
    path("<int:pk>", postDetail.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("comment/", commentListView.as_view(), name="comment_create"),
    path("home/", projects_and_news, name="home"),
    path('<int:post_id>/comments/update/<int:comment_id>/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post-update'),

]
