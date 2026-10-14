from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_view, name='inventory_list'),
    path('update/<int:product_id>/', views.update_stock, name='update_stock'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('order/update-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('order/confirm-payment/<int:order_id>/', views.confirm_payment, name='confirm_payment'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('order/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
]