from django.contrib import admin
from .models import Wish,WishItem
# Register your models here.
@admin.register(Wish)
class Wish(admin.ModelAdmin):
    list_display=['wish_id','emailAddress','date_added']
    list_filter=['date_added','emailAddress']
    list_display_links = ('wish_id', 'emailAddress')
    search_fields = ['emailAddress']
    readonly_fields = ['wish_id','emailAddress']

