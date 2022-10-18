from django.contrib import admin

# Register your models here.
from .models import Category,Product,Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','price','thumbnail']
    list_display_links = ['id','name','thumbnail'] #clickable fields
    list_filter = ['name','category']
    search_fields = ['id','name','category']


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Review)