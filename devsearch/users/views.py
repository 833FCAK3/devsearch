from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Profile

# Create your views here.


def profiles(request: WSGIRequest):
    return render(request, "users/profiles.html")
