from django.db import models
from datetime import datetime


class EventCategory(models.Model):

    event_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.event_category


class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_content = models.TextField()
    event_location = models.CharField(max_length=200)
    event_time = models.DateTimeField('event time')
    event_published = models.DateTimeField('date published', default=datetime.now())
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    event_category = models.ForeignKey(EventCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    event_slug = models.CharField(max_length=200, default=1)


    def __str__(self):
        return self.event_title
