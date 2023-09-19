from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from .models import Product, Contacts


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# def index(request):
#     products = Product.objects.all()  # Получение всех товаров из базы данных
#     return render(request, 'catalog/index.html', {'products': products})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


# def product_detail(request, id):
#     product = Product.objects.get(id=id)
#     return render(request, 'catalog/product_detail.html', {'product': product})


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'phone', 'message', )
    success_url = reverse_lazy('catalog:contacts')


# def contacts(request):
#     name = request.POST.get('name')
#     phone = request.POST.get('phone')
#     message = request.POST.get('message')
#
#     print(f"{name} ({phone}): {message}")
#
#     return render(request, 'catalog/contacts_form.html')



