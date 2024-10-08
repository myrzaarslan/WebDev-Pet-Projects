from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.new_page, name="newpage"),
    path("search", views.search, name="search"),
    path("edit", views.edit, name="edit"),
    path("editsub", views.editsub, name="editsub"),
    path("random", views.randompage, name="random"),
    path("wiki/<str:title>", views.title, name="title")
]
