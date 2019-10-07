from django.contrib import admin
from .models import Contact


class ContactAdminView(admin.ModelAdmin):
    list_display = ('listing_id', 'listing_title',
                    'contact_name', 'contact_date')
    list_per_page = 25
    list_display_links = ('listing_id', 'contact_name')
    search_fields = ('contact_name', 'listing_title')


admin.site.register(Contact, ContactAdminView)
