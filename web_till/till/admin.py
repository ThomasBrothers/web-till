from django.contrib import admin

from .models import Product, SaleTracker, Sale

admin.site.register(Product)
admin.site.register(SaleTracker)
admin.site.register(Sale)
