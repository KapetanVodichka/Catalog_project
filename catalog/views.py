from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .forms import ProductForm, ProductVersionForm, StyleFormMixin
from .models import Product, Contacts, ProductVersion


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['product_list']

        # Добавляем информацию об активной версии для каждого продукта
        for product in products:
            try:
                active_version = ProductVersion.objects.get(product=product, active_version=True)
                product.active_version = active_version
            except ProductVersion.DoesNotExist:
                product.active_version = None

        return context


# def index(request):
#     products = Product.objects.all()  # Получение всех товаров из базы данных
#     return render(request, 'catalog/index.html', {'products': products})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


# def product_detail(request, id):
#     product = Product.objects.get(id=id)
#     return render(request, 'catalog/product_detail.html', {'product': product})


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')
    template_name = 'catalog/includes/product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/includes/product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        try:
            active_version = ProductVersion.objects.get(product=product, active_version=True)
        except ProductVersion.DoesNotExist:
            active_version = None

        context['active_version'] = active_version
        return context

    def get_success_url(self):
        return reverse('catalog:update', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        response = super().form_valid(form)
        active_version_id = self.request.POST.get('active_version')

        if active_version_id:
            ProductVersion.objects.filter(product=self.object, active_version=True).update(active_version=False)
            ProductVersion.objects.filter(id=active_version_id).update(active_version=True)

        return response


class ProductVersionCreateView(CreateView):
    model = ProductVersion
    form_class = ProductVersionForm
    template_name = 'catalog/includes/version_form.html'

    def form_valid(self, form):
        product_id = self.kwargs['pk']  # Получаем id продукта из URL
        product = get_object_or_404(Product, pk=product_id)
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:update', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['active_version'] = product.active_version
        return context


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
