from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product


# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)

def product_by_id(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    data = {'product': {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active
    }}

    return JsonResponse(data)

def category_list(request):
    categories = Category.objects.all()
    data = {'categories': list(categories.values())}
    return JsonResponse(data)

def category_by_id(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    data = {'category': {
        "id": category.id,
        "name": category.name
    }}

    return JsonResponse(data)

def category_products(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    products = category.product_set.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)
