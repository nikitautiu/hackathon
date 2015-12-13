from django import forms
from django.core import validators
from django.utils import timezone

from .models import Event


class EventForm(forms.Form):
    error_messages={'required': 'Campul trebuie completat!',
        'invalid': 'Date invalide'}

    title = forms.CharField(label='Titlu', max_length=50)

    description = forms.CharField(label='Descriere', max_length=256,
        widget=forms.Textarea(attrs = {'rows': 3} ),
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
                        'invalid_choice': 'Introduceti o categorie valida!'})

    is_event = forms.BooleanField(label='Eveniment(oferta daca nu)',
        initial=True,
        error_messages={'required': 'Trebuie specificat!',
                        'invalid': 'True sau False!'})

    map_url = forms.URLField(label='Url locatie(Google Maps)', required=False,
        error_messages={'invalid': 'Invalid location'})

SEARCH_CRITERIAS = {
    'dhl' : 'Data(De la mare la mic)',
    'dlh' : 'Data(De la mic la mare)',

}

class SearchForm(forms.Form):
    keyword = forms.CharField(label='Cautare', max_length=50, required=False)
    from_date = forms.DateTimeField(label='Incepe dupa', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'aaaa-ll-zz [hh:mm]'}),
        error_messages={'required': 'Trebuie scrisa o data!',
                        'invalid': 'Introduceti o data valida!'})
    category = forms.ChoiceField(label='Categorie', required=False,
        choices=([('', 'All')] + list(Event.CATEGORIES.items())), initial='', 
        error_messages={'required': 'Trebuie data o categorie!',
                        'invalid': 'Introduceti o categorie valida!'})
    is_offer = forms.BooleanField(label='Doar oferte', required=False,
        error_messages={'required': 'Trebuie specificat!',
                        'invalid': 'True sau False!'})
    sort_criteria = forms.ChoiceField(label='Storta dupa', required=False,
        choices=([('', 'Nimic')] + list(SEARCH_CRITERIAS.items())), 
        error_messages={'invalid_choice': 'Introduceti un criteriu valid!'})

