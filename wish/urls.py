from django.urls import path
from . import views

app_name='wish'

urlpatterns = [
	path('add/<int:product_id>/', views.add_wish, name='add_wish'),
	path('',views.wish_detail, name='wish_detail'),
	path('remove/<int:product_id>/', views.wish_remove, name='wish_remove'),
	path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),
	
]