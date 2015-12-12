from django.contrib import admin

from .models import Event, Host

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Host)

