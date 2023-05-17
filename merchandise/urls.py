from django.urls import path
from . import views

urlpatterns = [
    path('', views.merchandise, name='merchandise'),
    path('<int:merchandise_id>/', views.merchandise_detail, name='merchandise_detail'),
    path('checkout/', views.checkout, name='checkout'),
]