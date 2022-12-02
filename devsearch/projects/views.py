from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProjectForm
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tags.all()
    return render(request, "projects/single-project.html", {"project": project_obj})


def create_project(request):
    form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/project_form.html", context)
