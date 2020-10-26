from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Contactee

class ContacteeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25 

admin.site.register(Contactee, ContacteeAdmin)