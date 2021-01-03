from django.urls import path
# from . import views
from .views import about_view, home_view


urlpatterns = [
    # path("home/",views.home_view)
    path("", home_view),
    path("about/", about_view)
]


