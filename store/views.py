from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def all_products(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True) # slug from the database is the slug from admin
    return render(request, 'store/products/detail.html', {'product':product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug) # returns one object from the database
    products = Product.objects.filter(category=category) # use that object to make a query on product database
    return render(request, 'store/products/category.html', {'category':category, 'products':products})
