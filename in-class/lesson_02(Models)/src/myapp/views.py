from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
  return HttpResponse("<h1> This is myapp home page</h1>")

def login_view(request):
  return HttpResponse("<h1> This is myapp login page</h1>")
