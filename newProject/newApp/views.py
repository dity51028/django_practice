from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def app_index(request):
    products = Product.objects.all()
    return render(request, 'newApp/app_index.html', {'products': products})

def about_view(request):
    return render(request, 'newApp/about_view.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'newApp/product_detail.html', {'product': product})
