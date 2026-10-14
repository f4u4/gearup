from django.contrib import admin
from django.utils.html import format_html
from .models import Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'order', 'product', 'status', 'created_at', 'show_image')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'description', 'reply')
    list_editable = ('status',)

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:4px;" />', obj.image.url)
        return "ไม่มีรูป"
    show_image.short_description = "หลักฐาน"