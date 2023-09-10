from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()  # Получение всех товаров из базы данных
    return render(request, 'catalog/index.html', {'products': products})


def contacts(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    print(f"{name} ({phone}): {message}")

    return render(request, 'catalog/contacts.html')


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'catalog/product_detail.html', {'product': product})
