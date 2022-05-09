from wish.models import Wish
from wish.models import WishItem
from wish.views import _wish_id

def counter(request): 
	item_count = 0
	if 'admin' in request.path:
		return{}
	else:
		try:
			wish = Wish.objects.filter(wish_id=_wish_id(request))
			wish_items = WishItem.objects.all().filter(wish=wish[:1])
			for wish_item in wish_items:
				item_count += wish_item.quantity
		except Wish.DoesNotExist:
			item_count = 0
	return dict(item_count = item_count)