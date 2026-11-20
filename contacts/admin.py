from django.contrib import admin
from .models import Contacts
from django.contrib.auth.models import User
# admin.site.register(Contacts)
@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'name',
        'city',
        'email',
        'phone',
        'created_at',
        'user'
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