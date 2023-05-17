from django.contrib import admin
from .models import Contact, feedback

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback_type', 'feedback')

