from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from home.models import Section, Detail


def main_call(request: HttpRequest) -> HttpResponse:
    sections = Section.objects.all()
    details = Detail.objects.all()
    context = {'sections': sections, 'details': details}
    return render(request, 'home.html', context)
