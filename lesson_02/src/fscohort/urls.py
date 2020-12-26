from django.urls import path
from .views import home_view, about_view, home

urlpatterns = [
    path("", home),
    path("home/", home_view),
    path("about/", about_view)
]
