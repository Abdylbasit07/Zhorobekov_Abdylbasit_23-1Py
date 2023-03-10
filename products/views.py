from django.shortcuts import render
from products.models import Product

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context = {
            'product': product,
            'reviews': product.reviews.all()
        }
        return render(request, 'products/detail.html', context=context)