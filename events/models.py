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
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True) # e null daca sepecifica numai data de inceput
    description = models.CharField(max_length=256)
    likes = models.IntegerField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_upcoming(self):
        return (self.start_date >= timezone.now() and 
            self.start_date <= timezone.now() + datetime.timedelta(days=2))

    def has_not_ended(self):
        return self.end_date >= timezone.now()
    has_not_ended.boolean = True



