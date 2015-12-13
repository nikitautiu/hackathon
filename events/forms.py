from django import forms
from django.core import validators
from django.utils import timezone

from .models import Event


class EventForm(forms.Form):
    error_messages={'required': 'Campul trebuie completat!',
        'invalid': 'Date invalide'}

    title = forms.CharField(label='Titlu', max_length=50)

    description = forms.CharField(label='Descriere', max_length=256,
        error_messages={'required': 'Trebuie scrisa o descriere!',
                        'invalid': 'Introduceti o descriere valida!'})

    start_date = forms.DateTimeField(label='Data de inceput(optional)', 
        widget=forms.TextInput(attrs={'placeholder': 'aaaa-ll-zz [hh:mm]'}),
        error_messages={'required': 'Trebuie scrisa o data!',
                        'invalid': 'Introduceti o data valida!'})

    end_date = forms.DateTimeField(label='Data de sfarsit', 
        widget=forms.TextInput(attrs={'placeholder': 'aaaa-ll-zz [hh:mm]'}), required=False,
        error_messages={'required': 'Trebuie scrisa o data!',
                        'invalid': 'Introduceti o data valida!'})

    category = forms.ChoiceField(label='Categorie',
        choices=Event.CATEGORIES.items(), 
        error_messages={'required': 'Trebuie data o categorie!',
                        'invalid': 'Introduceti o categorie valida!'})

class SearchForm(forms.Form):
    keyword = forms.CharField(label='Cautare', max_length=50)

