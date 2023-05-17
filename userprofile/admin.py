from django.contrib import admin
from .models import Userprofile

# Register your models here.
@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'city', 'state', 'pincode', 'created_on', 'updated_on')

    