from django.contrib import admin
from .models import Product, Category

# Admin 
admin.site.register(Product)
admin.site.register(Category)
