from django.http import HttpResponse
from django.shortcuts import render


def projects(request):
    return HttpResponse("Here are our projects")


def project(request, pk):
    return HttpResponse(f"SINGLE PROJECT {pk}")
