from django import forms

from . import models


class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = models.SupportTicket
        fields = ['username', 'email', 'text']

