from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Claim

# View สำหรับแสดงรายการใบแจ้งเคลมทั้งหมด
def claim_management(request):
    claims = Claim.objects.all().order_by('-created_at')
    return render(request, 'inventory/claim_management.html', {'claims': claims})

# View สำหรับอัปเดตสถานะและส่งข้อความตอบกลับ
def update_claim(request, claim_id):
    if request.method == 'POST':
        claim = get_object_or_404(Claim, id=claim_id)
        claim.status = request.POST.get('status')
        claim.reply = request.POST.get('reply')
        claim.save()
        messages.success(request, f"อัปเดตใบแจ้งเคลม #{claim.id} เรียบร้อยแล้ว")
        return redirect('claim_management')