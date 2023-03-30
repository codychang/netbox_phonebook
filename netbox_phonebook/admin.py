from django.contrib import admin
from .models import Function, Status, Number
from import_export.admin import ImportExportModelAdmin

@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ['pk','id','name','comments']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','name','comments']

@admin.register(Number)
class NumberAdmin(ImportExportModelAdmin):
    list_display = ['number','site','assignto','function','status']
    list_filter = ['site']
    search_fields = ['number']
