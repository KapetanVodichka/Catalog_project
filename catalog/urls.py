from django.urls import path
from catalog.views import index, contacts, product_detail


urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('product/<int:id>/', product_detail, name='product_detail'),
]
