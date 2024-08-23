from django.db import models


class NginxLogEntry(models.Model):
    objects = None
    ip_address = models.GenericIPAddressField()
    date_time = models.DateTimeField()
    http_method = models.CharField(max_length=10)
    url = models.CharField(max_length=2000)
    response_code = models.IntegerField()
    response_size = models.IntegerField()

    def __str__(self):
        return f"{self.ip_address} - {self.http_method} {self.url}"
