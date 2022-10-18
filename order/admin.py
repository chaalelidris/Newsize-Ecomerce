from django.contrib import admin
from .models import Order,OrderItem
from django.utils.html import format_html

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    row_id_fields = ['product'],


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','status','created_at','change', 'delete']
    list_display_links = ['id','first_name'] #clickable fields
    list_filter = ['status','created_at']
    search_fields = ['first_name','address','created_at']
    inlines = [OrderItemInline]

    #functions
    def change(self, Order):
        return format_html('<a class="btn" href="/admin/order/order/{}/change/">Change</a>', Order.id)
    def delete(self, Order):
        return format_html('<a class="btn" style="color:red;" href="/admin/order/order/{}/delete/">Delete</a>', Order.id)
    

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id','order','product','price','quantity']
    list_display_links = ['id','order'] #clickable fields
    list_filter = ['order','product']
    search_fields = ['id','order','product']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)