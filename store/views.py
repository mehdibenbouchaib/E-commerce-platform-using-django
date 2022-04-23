from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render

from store.models import Product


def index(request):
    product = Product.objects.all()
    return render(request, 'store/index.html', context={"products": product})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product":product})
