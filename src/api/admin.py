from django.contrib import admin

from . import models


@admin.register(models.FinancailUnitsType)
class FinancailUnitsTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.FinancialUnit)
class FinancailUnitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fin_type', 'active')
    search_fields = ('name',)
