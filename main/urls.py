from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("post/create/", views.create_post, name="create-post"),
    path("post/<int:pk>/delete/", views.delete_post, name="delete-post"),
    path("post/<int:pk>/update/", views.update_post, name="update-post"),
    path("delete/", views.delete, name="delete")    
]