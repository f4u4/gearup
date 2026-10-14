from django.urls import path
from . import views

urlpatterns = [
    path('management/', views.claim_management, name='claim_management'),
    path('update/<int:claim_id>/', views.update_claim, name='update_claim'),
]