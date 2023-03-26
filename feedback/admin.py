from django.contrib import admin

from feedback.models import FeedbackModel


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'first_name',
        'last_name',
        'body'
    )


admin.site.register(FeedbackModel, FeedbackAdmin)