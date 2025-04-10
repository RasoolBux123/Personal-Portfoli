
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('about/', views.about , name="about_page"),
    path('project/', views.project , name="about_page"),
    path('contact/', views.contact , name="about_page"),
]
