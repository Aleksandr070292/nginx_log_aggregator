from rest_framework import viewsets
from .models import NginxLogEntry
from .serializers import NginxLogEntrySerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class NginxLogEntryViewSet(viewsets.ModelViewSet):
    queryset = NginxLogEntry.objects.all()
    serializer_class = NginxLogEntrySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('ip_address', 'url')
    ordering_fields = ('date_time', 'response_code')
