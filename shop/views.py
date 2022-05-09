from django.shortcuts import render, get_object_or_404

from shop.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib import messages
from django.urls import reverse
# Category view

def allProdCat(request, c_slug=None): 

    c_page = None  
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
                                                 
    else:
        products_list = Product.objects.all().filter(available=True)
    ''' Pagination'''
    paginator = Paginator(products_list, 12)  # limiting 12 products per category page
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category': c_page, 'products': products})


# Product View

def ProdCatDetail(request, c_slug, product_slug): 
    
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
        ctg= Category.objects.get(name=product.category)
        related_products = Product.objects.filter(category=ctg)
        
        context = {
            'product':product,
            'related_products':related_products
        }

    except Exception as e:
        raise e
    return render(request, 'product.html', context)

def wish_prod(request,product_slug):
    try:
        product1 = Product.objects.get(category__slug=c_slug, slug=product_slug)
        username= User.get(name=username)

        wish= Product.objects.filter(name=username)
    
        context = {
            'product':product,
            'wish':wish
        }
    except Exception as e:
        raise e
    return render(request, 'sample.html', context)
