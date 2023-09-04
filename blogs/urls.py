from django.urls import path
from .views import blogList,followerList,Category_list,BlogFollowersView,searchView ,CreateBlog,UpdateBlog,FollowBlog,UnfollowBlog , Friends

urlpatterns = [
    path("", blogList, name="blog_list"),
    path("<int:pk>/", blogList, name="blog_detail"),
    path("followers/", followerList.as_view(), name="follower_list"),
    path("categories/", Category_list.as_view(), name="categories_list"),
    path("userfollowing/", BlogFollowersView.as_view(), name="blog_followers"),
    path("search/",searchView, name="search"),
    path("createblog/", CreateBlog, name="createblog"),
    path('update/', UpdateBlog, name='blog-update'),
    path('follow/', FollowBlog.as_view(), name='follow-blog'),
    path('unfollow/<int:blog_id>/', UnfollowBlog.as_view(), name='unfollow-blog'),
    path('user_friends/',Friends.as_view(),name="user-friends")
]
