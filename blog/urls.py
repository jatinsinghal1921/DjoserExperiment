from django.urls import path
from . import views

urlpatterns = [
    path("listAll/", views.listBlog.as_view())
]
