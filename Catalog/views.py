from django.shortcuts import render
import json


def index(request):
    return render(request, 'Catalog/index.html')


def contacts(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    print(f"{name} ({phone}): {message}")

    return render(request, 'Catalog/contacts.html')
