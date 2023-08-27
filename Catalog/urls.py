from django.urls import path
from Catalog.views import index, contacts


urlpatterns = [
    path('', index),
    path('contacts/', contacts)
]
