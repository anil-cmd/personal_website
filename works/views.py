from django.shortcuts import render
from .models import Projects

# Create your views here.


def projects(request):
    works = Projects.objects.all()
    return render(request, 'works.html', {'works': works})


def resume(request):
    return render(request, 'resume.html')
