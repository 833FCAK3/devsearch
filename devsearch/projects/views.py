from django.http import HttpResponse
from django.shortcuts import render


projects_list = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website",
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "A personal website to write articles and display work",
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "An open source project built by the community",
    },
]


def projects(request):
    page = "projects"
    number = 10
    context = {"page": page, "number": number, "projects": projects_list}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = None
    for i in projects_list:
        if i["id"] == pk:
            project_obj = i
    return render(request, "projects/single-project.html", {"project": project_obj})
