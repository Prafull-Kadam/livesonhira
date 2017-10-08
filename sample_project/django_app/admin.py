from django.contrib import admin
from .models        import (profile)

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'city', 'mobile_no')
    list_filter   = ('city', 'mobile_no')