from django.contrib import admin
from projectmanagent.models import *

# Register your models here.
admin.site.site_header = "自动化管理后端"
admin.site.index_title = "項目管理"
admin.site.site_title = "AutoTest"

@admin.register(ProjectManager)
class ProjectManagerConfig(admin.ModelAdmin):
    list_display =["name","start_time","end_time"]


@admin.register(ProjectServer)
class ProjectServerConfig(admin.ModelAdmin):
    list_display = ["name","ip_url","custom_variable","desc"]



@admin.register(ProjectDataServer)
class ProjectDataServerConfig(admin.ModelAdmin):
    list_display =  ["name","port","ip"]
