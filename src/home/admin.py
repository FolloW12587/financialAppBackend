from django.contrib import admin
from django.utils.timezone import now

from . import models


@admin.register(models.SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    readonly_fields = ("status", "time_opened", "time_closed")
    list_display = ("id", "username", "email", "status", "time_opened", "time_closed")
    actions = ["process_ticket", "close_ticket"]


    @admin.action(description='Взять тикет в обработку')
    def process_ticket(modeladmin, request, queryset):
        for obj in queryset:
            if obj.status == models.SupportTicket.OPENED:
                obj.status = models.SupportTicket.PROCESSING
                obj.save()

    @admin.action(description='Закрыть тикет')
    def close_ticket(modeladmin, request, queryset):
        for obj in queryset:
            if obj.status == models.SupportTicket.PROCESSING:
                obj.status = models.SupportTicket.CLOSED
                obj.time_closed = now()
                obj.save()
