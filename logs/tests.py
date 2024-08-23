from django.test import TestCase
from logs.models import NginxLogEntry


class NginxLogEntryTestCase(TestCase):
    def setUp(self):
        NginxLogEntry.objects.create(
            ip_address='192.168.0.1',
            date_time='2024-08-22T12:34:56Z',
            http_method='GET',
            url='/index.html',
            response_code=200,
            response_size=1024,
        )

    def test_log_entry_creation(self):
        entry = NginxLogEntry.objects.get(ip_address='192.168.0.1')
        self.assertEqual(entry.url, '/index.html')
