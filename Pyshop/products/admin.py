from django.contrib import admin
from .models import Product

class ProductAd(admin.ModelAdmin):
    list_display = ('name','stock','price')
admin.site.register(Product,ProductAd)