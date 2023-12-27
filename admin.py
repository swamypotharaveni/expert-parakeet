from django.contrib import admin
from myapp1.models import CustomUser
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group


admin.site.register(CustomUser)
admin.site.unregister(Group)
# Register your models here.
