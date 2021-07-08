from django.shortcuts import render
from .models import Product

# Views

def all_products(request):
    """ Show All Products. Sorting and quries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)