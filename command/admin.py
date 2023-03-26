from django.contrib import admin

from command.models import Command


class CommandAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'role_in_the_project',
        'photo'
    )


admin.site.register(Command, CommandAdmin)