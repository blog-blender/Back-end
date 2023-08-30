from django.urls import path
from .views import blogList, blogDetail,followerList,Category_list,BlogFollowersView,searchView ,CreateBlog

urlpatterns = [
    path("", blogList.as_view(), name="blog_list"),
    path("<int:pk>/", blogDetail.as_view(), name="blog_detail"),
    path("followers/", followerList.as_view(), name="follower_list"),
    path("categories/", Category_list.as_view(), name="categories_list"),
    path("userfollowing/", BlogFollowersView.as_view(), name="blog_followers"),
    path("search/",searchView, name="search"),
    path("createblog/", CreateBlog.as_view(), name="createblog"),

]
