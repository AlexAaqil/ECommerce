from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.filter(featured=True).order_by("-date")

    context = {
        "products": products
    }

    return render(request, 'core/index.html', context)