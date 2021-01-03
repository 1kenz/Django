from django.urls import path
# from . import views
from .views import home_view


urlpatterns = [
    # path("home/",views.home_view)
    path("home/",home_view)
]


