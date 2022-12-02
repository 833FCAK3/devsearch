from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ProjectForm
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {"project": project_obj})


def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object": project}
    return render(request, "projects/delete_template.html", context)
