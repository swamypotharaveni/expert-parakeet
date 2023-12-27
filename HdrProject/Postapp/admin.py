from django.contrib import admin
from .models import CustomUser
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group
class CustomuserDetails(admin.ModelAdmin):
    list_display = ['username','updated_at','bio','image_tag']

admin.site.register(CustomUser,CustomuserDetails)
admin.site.unregister(Group)
# Register your models here.