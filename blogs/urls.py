from django.urls import path
from .views import blogList,followerList,Category_list,BlogFollowersView,searchView ,CreateBlog,BlogUpdateView,FollowBlog,UnfollowBlog

urlpatterns = [
    path("", blogList, name="blog_list"),
    path("<int:pk>/", blogList, name="blog_detail"),
    path("followers/", followerList.as_view(), name="follower_list"),
    path("categories/", Category_list.as_view(), name="categories_list"),
    path("userfollowing/", BlogFollowersView.as_view(), name="blog_followers"),
    path("search/",searchView, name="search"),
    path("createblog/", CreateBlog, name="createblog"),
    path('<int:blog_id>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('follow/', FollowBlog.as_view(), name='follow-blog'),
    path('unfollow/<int:blog_id>/', UnfollowBlog.as_view(), name='unfollow-blog'),
]
