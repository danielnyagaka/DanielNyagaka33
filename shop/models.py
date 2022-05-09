from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.forms import ModelForm

class Category(models.Model):
	name = models.CharField(max_length=250,unique=True)
	slug = models.SlugField(max_length=250,unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category',blank=True) 
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):  
		return reverse('shop:products_by_category', args=[self.slug]) 

	def __str__(self): 
		return '{}'.format(self.name)


class Product(models.Model):
	
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True) 
	description = models.TextField(blank=True)
	#product_id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 
	price = models.DecimalField(max_digits=10, decimal_places=2)
	cut_through_price=models.DecimalField(max_digits=10, decimal_places=2,default="999")
	discount=models.IntegerField(default="1")
	
	image = models.ImageField(upload_to='product', blank=True)
	image1 = models.ImageField(upload_to='product', blank=True)
	image2 = models.ImageField(upload_to='product', blank=True)
	image3 = models.ImageField(upload_to='product', blank=True)
	image4 = models.ImageField(upload_to='product', blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True) 
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)

	favourite = models.ManyToManyField(User ,related_name='favourite',blank=True)
	


	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
	
	def __str__(self):
		return '{}'.format(self.name)