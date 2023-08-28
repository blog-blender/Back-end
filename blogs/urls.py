from django.urls import path
from .views import blogList, blogDetail,followerList,FollowedBlogsView

urlpatterns = [
    path("", blogList.as_view(), name="blog_list"),
    path("<int:pk>/", blogDetail.as_view(), name="blog_detail"),
    path("followers/", followerList.as_view(), name="follower_list"),
    path("followersBlog/", FollowedBlogsView.as_view(), name="followers_blog"),

]
