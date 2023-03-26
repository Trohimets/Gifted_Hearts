from django.contrib import admin

from friends.models import FriendsModel


class FriendsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'photo',
        'first_name',
        'last_name',
        'role_in_the_project',
    )
    list_display_links = (
        'first_name',
        'last_name',
    )


admin.site.register(FriendsModel, FriendsAdmin)
