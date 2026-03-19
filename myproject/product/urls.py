from django.urls import path
from .views import get_product, create_product

urlpatterns = [
    path('all/', get_product, name='get_product'),
    path('create/', create_product, name='create_product')
]
