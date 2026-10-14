from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    readonly_fields = ('total_price',)
    list_display = ('id', 'customer_name', 'total_price', 'status', 'is_paid')

admin.site.register(Order, OrderAdmin)