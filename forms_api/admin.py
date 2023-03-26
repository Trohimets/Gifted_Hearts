from django.contrib import admin

from forms_api.models import FeedBackSuggestion, ApplicationsForVolunteering, RegistrationForEvents


class FeedBackSuggestionAdmin(admin.ModelAdmin):
    ...


class ApplicationsForVolunteeringAdmin(admin.ModelAdmin):
    ...


class RegistrationForEventsAdmin(admin.ModelAdmin):
    ...


admin.site.register(FeedBackSuggestion, FeedBackSuggestionAdmin)
admin.site.register(ApplicationsForVolunteering, ApplicationsForVolunteeringAdmin)
admin.site.register(RegistrationForEvents, RegistrationForEventsAdmin)
