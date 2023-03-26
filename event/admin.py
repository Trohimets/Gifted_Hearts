from django.contrib import admin

from event.models import EventModel, PhotoEventModel


class EventPhotoAdmin(admin.StackedInline):
    model = PhotoEventModel


class EventAdmin(admin.ModelAdmin):
    inlines = [EventPhotoAdmin]


admin.site.register(EventModel, EventAdmin)
