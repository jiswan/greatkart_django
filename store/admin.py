from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price','stock','category','modified_time','is_avilable')
# Register your models here.
admin.site.register(Product,ProductAdmin)