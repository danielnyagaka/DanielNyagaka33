from django.db import models
from shop.models import Product

class Wish(models.Model):
	wish_id = models.CharField(max_length=250, blank=True)
	emailAddress = models.EmailField(max_length = 250, blank = True, verbose_name = 'Email Address')
	date_added = models.DateField(auto_now_add=True)

	class Meta:
		db_table = 'Wish' 
		ordering = ['date_added']

	def __str__(self):
		return self.wish_id


class WishItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE) 
	wish = models.ForeignKey(Wish, on_delete=models.CASCADE)
	quantity = models.IntegerField(default="1")
	price = models.IntegerField(default="0")
	
	class Meta:
		db_table = 'WishItem'
	def __str__(self):
		return self.product


