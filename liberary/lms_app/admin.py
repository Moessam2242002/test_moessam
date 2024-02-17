from django.contrib import admin
from .models import *
# Register your models here.
class category(admin.ModelAdmin):
    list_display = ['name']
class books(admin.ModelAdmin):
    list_display=['book_name','auther','book_image','auther_image','pages','price','rental_price_day','rental_period','active','status','category']
    list_display_links=['book_name']
    list_editable=['auther','book_image','auther_image','pages','price','rental_price_day','rental_period','active','status','category']
admin.site.register(Category,category)
admin.site.register(Books,books)