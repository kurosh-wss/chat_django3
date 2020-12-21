from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path(route='', view=views.home, name="home"),
    path(route="posts/", view=views.PostListView.as_view(), name="posts"),
    path(route="post/<int:pk>/", view=views.PostDetailView.as_view(), name='post'),
]