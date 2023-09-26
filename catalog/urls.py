from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsCreateView, ProductCreateView, ProductUpdateView,\
    ProductVersionCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('update/<int:pk>/create_version/', ProductVersionCreateView.as_view(), name='create_product_version'),
]