from django.shortcuts import render
from .models import Lines

# Create your views here.


def home(request):
    lines = Lines.objects.all()
    return render(request, 'home.html', {'lines': lines})
