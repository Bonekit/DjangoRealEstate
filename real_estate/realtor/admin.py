from django.contrib import admin
from .models import Realtors


@admin.register(Realtors)
class RealtorsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_mvp')
    list_editable = ('is_mvp',)
    list_display_links = ('first_name', 'last_name')
    search_fields = ('last_name',)
