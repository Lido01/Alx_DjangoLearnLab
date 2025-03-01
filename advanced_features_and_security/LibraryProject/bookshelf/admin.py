from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
    ordering = ["email"]
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)