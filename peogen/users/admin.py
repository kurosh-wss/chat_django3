from django.contrib import admin
from .models import Profile

# class ProfileAdmin(admin.ModelAdmin):
#     fields

admin.site.register(Profile)
