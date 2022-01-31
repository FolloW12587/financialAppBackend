from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def terms(request):
    return render(request, 'terms.html')

def support(request):
    if request.method == 'POST':
        form = forms.SupportTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return  render(request, 'support_base.html')
    else:
        form = forms.SupportTicketForm()

    return render(request, 'support_form.html', {'form': form})