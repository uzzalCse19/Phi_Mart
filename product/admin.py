from django.contrib import admin

# Register your models here.
from django.contrib import admin
from product.models import Product, Category, Review
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)