from django.contrib import admin

from basics.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Contact, ContactAdmin)
