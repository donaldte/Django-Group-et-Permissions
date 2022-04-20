from django.contrib import admin

# Register your models here.
from .models import PremiumProduct, Product
admin.site.register(Product)
admin.site.register(PremiumProduct)