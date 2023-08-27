from django.urls import path
from .views_front import (
    blogCreateView,
    blogDeleteView,
    blogDetailView,
    blogListView,
    blogUpdateView,
)

urlpatterns = [
    path("", blogListView.as_view(), name="blog_list"),
    path("<int:pk>/", blogDetailView.as_view(), name="blog_detail"),
    path("create/", blogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/update/", blogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", blogDeleteView.as_view(), name="blog_delete"),
]
