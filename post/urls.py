from django.urls import path
from .views import HomePage, AddPost, PostDetailView, PostDeleteView, PostEditView

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("<int:pk>/delete_post/", PostDeleteView.as_view(), name="delete_post"),
    path("<int:pk>/edit/", PostEditView.as_view(), name="edit_post"),
    path("<int:pk>/detail/", PostDetailView.as_view(), name="detail_post"),
]
