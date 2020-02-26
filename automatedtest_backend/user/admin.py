from django.contrib import admin

# Register your models here.
from django.apps import AppConfig

from user.models import ApiUser,User

admin.site.site_header = "自动化管理后端"
admin.site.index_title = "自动化管理"
admin.site.site_title = "AutoTest"

@admin.register(ApiUser)
class ApiUserConfig(admin.ModelAdmin):
    list_display = ['number','created','updated']

@admin.register(User)
class UserConfig(admin.ModelAdmin):
    list_display =  ['username']