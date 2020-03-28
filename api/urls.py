from django.urls import path
from api import views

urlpatterns = [
    path('products/', ),
    path('products/<int:id>', ),
    path('categories/', ),
    path('categories/<int:id>', ),
    path('categories/<int:id>/products', )
]