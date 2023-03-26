from django.contrib import admin

from company.models import CompanyModel


class CompanyModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'desc',
        'logo'
    )


admin.site.register(CompanyModel, CompanyModelAdmin)