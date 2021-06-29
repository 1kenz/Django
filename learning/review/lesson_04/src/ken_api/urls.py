from typing import Pattern
from django.urls import path
from .views import ken_api, student_list

urlpatterns = [
    path("", ken_api),
    path("list-api/", student_list)
]

