from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category
from django.db.models import Count


def index(request):
    products = Product.objects.filter(product_status="published", featured=True).order_by("-date")

    context = {
        "products": products
    }

    return render(request, 'core/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-date")

    context = {
        "products": products
    }

    return render(request, 'core/product_list.html', context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    product_images = product.product_images.all()
    related_products = Product.objects.filter(category=product.category).exclude(pid=pid)[:4]

    context = {
        "product" : product,
        "product_images" : product_images,
        "related_products" : related_products,
    }

    return render(request, "core/product_detail.html", context)


def category_list_view(request):
    categories = Category.objects.annotate(product_count=Count('product'))

    context = {
        "categories" : categories
    }

    return render(request, "core/category_list.html", context)


def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category" : category,
        "products" : products,
    }

    return render(request, "core/category_product_list.html", context)


def add_to_cart(request):
    cart_products = {

    }
    cart_products[str(request.GET['id'])] = {        
        'quantity' : request.GET['quantity'],
        'title' : request.GET['title'],
        'price' : request.GET['price'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['quantity'] = int(cart_products[str(request.GET['id'])]['quantity'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_products)
            request.session['cart_data_obj'] = cart_data
    else:
        request.session['cart_data_obj'] = cart_products
    return JsonResponse({"data":request.session['cart_data_obj'], 'total_cart_items':len(request.session['cart_data_obj'])})
