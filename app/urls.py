from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),
]