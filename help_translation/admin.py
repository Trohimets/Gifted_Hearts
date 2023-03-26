from django.contrib import admin


from help_translation.models import HelpTranlationModel, AutoPayModel


class HelpTranlationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone' ,
        'email',
        'amount',
        'type_transfer',
        'one_time',
        'monthly',
        'comment'
    )


admin.site.register(HelpTranlationModel, HelpTranlationAdmin)

class AutoPayAdmin(admin.ModelAdmin):
    list_display = (
         'uuid',
         'email',
         'amount',
         'date_now',
         'date_next_month'
    )

admin.site.register(AutoPayModel, AutoPayAdmin)