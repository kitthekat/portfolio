from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from projects.models import Project


def project_index(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()  # query
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request: HttpRequest, pk: str) -> HttpResponse:
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})


