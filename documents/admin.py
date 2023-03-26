from django.contrib import admin
from documents.models import Document


class DocumentModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
        'link',
        'description',
    )

admin.site.register(Document, DocumentModelAdmin)