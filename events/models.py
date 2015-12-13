import datetime

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.


class Host(models.Model):
    # mode l pentru gazde de evenimente
    user = models.OneToOneField(User, on_delete=models.CASCADE) # relationare 
    name =  models.CharField(max_length=50)


class Event(models.Model):
    CATEGORIES ={
        'pa': 'Party',
        'fo': 'Gastronomie',
        'sp': 'Sport',
        'ed': 'Educativ',
        're': 'Religios',
        'ba': 'Bautura',
        'mu': 'Muzical',
        'fi': 'Film',
    }

    title = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True) # e null daca sepecifica numai data de inceput
    description = models.CharField(max_length=256)
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=2,
                                 choices=CATEGORIES.items())
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    is_event = models.BooleanField(default=True)

    def is_upcoming(self):
        return (self.start_date >= timezone.now() and 
            self.start_date <= timezone.now() + datetime.timedelta(days=2))

    def has_not_ended(self):
        return self.end_date >= timezone.now()
    has_not_ended.boolean = True


def search_events(keyword=None, from_date=None, category=None, 
    is_offer=False, sort_criteria=None):
    queryset = Event.objects.filter(end_date__gt=timezone.now())
    if keyword is not None:
        queryset = queryset.filter(models.Q(description__contains=keyword) | 
            models.Q(title__contains=keyword) | models.Q(category__exact=keyword))
    if from_date is not None:
        queryset = queryset.filter(end_date__gt=from_date)
    if category != '':
        queryset = queryset.filter(category__exact=category)
   
    if is_offer:
        queryset = queryset.filter(is_event=False)
    if sort_criteria is not None:
        if sort_criteria == 'dhl':
            queryset = queryset.order_by('-start_date')
        elif sort_criteria == 'dlh':
            queryset = queryset.order_by('start_date')
    return queryset

