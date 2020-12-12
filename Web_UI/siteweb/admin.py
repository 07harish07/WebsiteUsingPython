from django.contrib import admin
from .models import News, Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fullname',
        'email',
        'number'
    )
    search_fields = (
        'id',
        'fullname',
        'email',
    )


admin.site.register(News)
admin.site.register(Contact, ContactAdmin)
