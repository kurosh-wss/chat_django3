from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path(route='', view=views.Home.as_view(), name="home"),
    path(route="about/", view=views.About.as_view(), name="about"),
    path(route="contact/", view=views.Contact.as_view(), name="contact"),
    path(route="portfolio/", view=views.Portfolio.as_view(), name="portfolio"),
    path(route="posts/", view=views.PostListView.as_view(), name="posts"),
    path(route="post/<int:pk>/", view=views.PostDetailView.as_view(), name='post'),

]