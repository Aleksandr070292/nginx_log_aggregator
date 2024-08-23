from django.contrib import admin
from .models import NginxLogEntry


@admin.register(NginxLogEntry)
class NginxLogEntryAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'date_time', 'http_method', 'url', 'response_code', 'response_size')
    list_filter = ('http_method', 'response_code', 'date_time')
    search_fields = ('ip_address', 'url')
    