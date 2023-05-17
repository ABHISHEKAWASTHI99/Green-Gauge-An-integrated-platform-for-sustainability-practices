from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blogs'),
    path('<int:user_id>/', views.details, name='details'),
]
