from re import search
from django.contrib import admin

from . import models


@admin.register(models.FinancailUnitsType)
class FinancailUnitsTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.FinancialUnit)
class FinancailUnitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fin_type', 'active', 'app')
    search_fields = ('name',)


@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'app')
    search_fields = ('name',)


@admin.register(models.App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.LeadFormData)
class LeadFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'sum')
    search_fields = ('name',)
