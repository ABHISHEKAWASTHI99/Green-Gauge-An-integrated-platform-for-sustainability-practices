from django.contrib import admin
from .models import *

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('level', 'title', 'slug', 'body', 'duration', 'created_at', 'updated_at')

@admin.register(User_Task)
class User_TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge', 'completed', 'date')

@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'img')
    
