from django.contrib import admin
from .models import InterfaceModule, InterfaceModel, KeysModel


# Register your models here.

@admin.register(InterfaceModule)
class InterfaceModuleConfig(admin.ModelAdmin):
    list_display = ["name", "project", "is_delete","top"]

@admin.register(InterfaceModel)
class InterfaceModel(admin.ModelAdmin):
    list_display = ["name","intermodule"]

@admin.register(KeysModel)
class KeysModelConfig(admin.ModelAdmin):
    list_display = ['name','count','params_constraint',"keytype"]