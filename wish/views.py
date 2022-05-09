from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Wish, WishItem
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings


def _wish_id(request):  
    wish = request.session.session_key
    if not wish:
        wish = request.session.create()
    return wish


def add_wish(request, product_id):
    product = Product.objects.get(id=product_id)
    try:  
        wish = Wish.objects.get(wish_id=_wish_id(request))
    
    except Wish.DoesNotExist:
        wish = Wish.objects.create(
            wish_id=_wish_id(request)
        )
        wish.save()
    try:
        wish_item = WishItem.objects.get(product=product, wish=wish)  
        if wish_item.quantity < wish_item.product.stock:
            wish_item.quantity += 1
        wish_item.save()
    except WishItem.DoesNotExist:
        wish_item = WishItem.objects.create(
            product=product,
            quantity=1,
            wish=wish
        )
        wish_item.save()
    return redirect('wish:wish_detail')





def wish_remove(request, product_id):  
    wish = Wish.objects.get(wish_id=_wish_id(request))
    product = get_object_or_404(Product, id=product_id)
    wish_item = WishItem.objects.get(product=product, wish=wish)
    if wish_item.quantity > 1:
        wish_item.quantity -= 1
        wish_item.save()
    else:
        wish_item.delete()
    return redirect('wish:wish_detail')


def full_remove(request, product_id):  
    wish = Wish.objects.get(wish_id=_wish_id(request))
    product = get_object_or_404(Product, id=product_id)
    wish_item = WishItem.objects.get(product=product, wish=wish)
    wish_item.delete()
    return redirect('wish:wish_detail')




def wish_detail(request, total=0, counter=0, additem=0, wish_items=None):  
    try:
        wish = Wish.objects.get(wish_id=_wish_id(request))
        wish_items = WishItem.objects.filter(wish=wish)
    except ObjectDoesNotExist:
        pass
    if request.method == 'POST':  
        try:
            email = request.POST['email']

            ''' Creating the Order '''
            try:
                wish_details = Wish.objects.create(emailAddress=email)
                wish_details.save()
                for wish_item in wish_items:  
                    wi = WishItem.objects.create(
                        product=wish_item.product.name,
                        price=wish_item.product.price,
                        wish=wish_details
                    )  
                    wi.save()

                return redirect('wish:thanks')
            except ObjectDoesNotExist:
                pass
        except:
            return False

    return render(request, 'wish.html', dict(wish_items=wish_items))

