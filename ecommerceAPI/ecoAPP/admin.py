from django.contrib import admin

from .models import *

@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    """description: Admin interface model for Category"""
    
    list_display = ('id', 'username')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """description: Admin interface model for Category"""

    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """description: Admin interface model for Product"""

    list_display = ('id', 'name', 'category', 'price', 'discount_price', 'cover_image')

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    """ description: Admin interface model for Basket"""

    list_display = ('id', 'user', 'total_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """"description: Admin interface model for Order"""
    inlines = [OrderProductInline]
    list_filter = ['paid']
    search_fields = ['user__username']
    list_display = ('user', 'total_price', 'date', 'delivery_address', 'paid')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """"description: Admin interface model for Payment"""

    list_display = ('id', 'order', 'amount', 'payment_date')