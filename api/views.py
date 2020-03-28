from django.shortcuts import render
from api.models import Product
from api.models import Category
from django.http.response import JsonResponse


def product_list(request):
    products = Product.objects.all()
    products_json = [products.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    product = Product.objects.all(id = product_id)
    return JsonResponse(product, safe=False)

def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)

def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())