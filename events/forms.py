from django import forms
from django.core import validators
from django.utils import timezone

from .models import Event

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid value'
}

class EventForm(forms.Form):
    error_messages={'required': 'Campul trebuie completat!',
        'invalid': 'Date invalide'}

    title = forms.CharField(label='Titlu', max_length=50)
    description = forms.CharField(label='Descriere', max_length=256,
        error_messages={'required': 'Trebuie scrisa o descriere!'})
    start_date = forms.DateTimeField(label='Data de inceput')
    end_date = forms.DateTimeField(label='Data de sfarsit', required=False)
