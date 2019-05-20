from django.contrib import admin
from .models import Event, EventCategory
from tinymce.widgets import TinyMCE
from django.db import models


class EventAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date/location", {'fields': ["event_title", "event_time", "event_location"]}),
        ("Content", {"fields": ["event_content"]}),
        ("URL", {'fields': ["event_slug"]}),
        ("Categories", {'fields': ["event_category"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }



admin.site.register(EventCategory)
admin.site.register(Event,EventAdmin)