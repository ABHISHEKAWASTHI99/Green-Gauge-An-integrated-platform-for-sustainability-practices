from django.urls import path
from . import views
urlpatterns = [
    path('', views.task, name='tasks'),
    path('challenge/complete/<int:id>/', views.complete_task, name='challenge_complete'),
    path('challenge/detail/<int:pk>/', views.challenge_detail, name='challenge_detail'),
    path('report/', views.report, name='report')
]