from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("Hello from HOME Page !!!")

def about(request):
    return HttpResponse("Hello from ABOUT Page")