from django.contrib import admin
from .models import Contacts

# admin.site.register(Contacts)
@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'city',
        'email',
        'phone',
        'created_at',
    )

    search_fields = (
        'name',
        'email',    
        'phone',
    )
    
    list_filter = (
        'city',
        'created_at',
    )

    ordering = ('name',)