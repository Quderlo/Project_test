from django.shortcuts import render, get_object_or_404
from .models import Product 
from django.utils import timezone

def product_list(request):
	products = Product.objects.filter(date_create__lte=timezone.now()).order_by('date_create')
	return render(request, 'blog/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'blog/product_detail.html', {'product': product})
