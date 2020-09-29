from django.shortcuts import render
from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST':

        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')

        ins = Contact(email=email, name=name, message=message)
        ins.save()
        return render(request, 'contact.html', {'name': name})

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
