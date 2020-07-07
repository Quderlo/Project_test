from django.contrib import admin
from .models import Product, Writer, Category

admin.site.register(Product)
admin.site.register(Writer)
admin.site.register(Category)