from django.db import models
from inventory.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอการยืนยัน'),
        ('confirmed', 'ยืนยันออเดอร์แล้ว'),
        ('shipped', 'จัดส่งแล้ว'),
        ('cancelled', 'ยกเลิก'),
    ]
    customer_name = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def update_total_price(self):
        total = sum(item.product.price * item.quantity for item in self.items.all())
        self.total_price = total
        self.save()

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.update_total_price()

    def delete(self, *args, **kwargs):
        order = self.order
        super().delete(*args, **kwargs)
        order.update_total_price()

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
