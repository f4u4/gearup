from django.db import models
from inventory.models import Product
from orders.models import Order

class Claim(models.Model):
    STATUS_CHOICES = [
        ('Open', 'รอตรวจสอบ'),
        ('Approved', 'อนุมัติ/กำลังดำเนินการ'),
        ('Rejected', 'ปฏิเสธการเคลม'),
        ('Completed', 'เคลมสำเร็จ'),
    ]

    customer_name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    reply = models.TextField(blank=True, null=True)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name="ออเดอร์")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name="สินค้า")
    image = models.ImageField(upload_to='claims/', blank=True, null=True, verbose_name="รูปหลักฐาน")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Claim #{self.id} - {self.customer_name}"