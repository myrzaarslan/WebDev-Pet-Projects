from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("unipage/<str:uni>", views.university, name="university"),
    path("pomodoro", views.pomodoro, name='pomodoro'),

    #API routes
    path('api/the_universities/', views.the_universities_list, name='the_universities_list'),
    path('api/qs_universities/', views.qs_universities_list, name='qs_universities_list'),
]

"""
With Subject Name: api/universities/?subjectname=Computer%20Science
With Page and Items Per Page: api/universities/?page=1&items_per_page=5
With All Parameters: api/universities/?subjectname=Engineering&page=2&items_per_page=20
"""