from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("products/", views.product_list, name = "allProducts"),
    path("products/<int:product_id>", views.product_by_id, name = "productById"),
    path("categories/", views.category_list, name = "allCategories"),
    path("categories/<int:category_id>", views.category_by_id, name = "categoryById"),
    path("categories/<int:category_id>/products", views.category_products, name = "categoryProducts")
]