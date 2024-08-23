import re
from datetime import datetime
from django.core.management import BaseCommand
from logs.models import NginxLogEntry
import requests
from django.db import transaction

class Command(BaseCommand):
    help = 'Парсинг Nginx лога и сохранение в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL лог файла')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        response = requests.get(url)
        log_data = response.text.splitlines()

        log_pattern = re.compile(
            r'{"time": "(?P<date_time>[^"]+)", "remote_ip": "(?P<ip>[^"]+)", "remote_user": "[^"]*", '
            r'"request": "(?P<method>[A-Z]+) (?P<url>[^ ]+) HTTP/[0-9\.]+", "response": (?P<status_code>\d+), '
            r'"bytes": (?P<size>\d+|-)}'
        )

        entries = []

        for line in log_data:
            match = log_pattern.match(line)
            if match:
                date_time = datetime.strptime(
                    match.group('date_time'), '%d/%b/%Y:%H:%M:%S %z'
                )
                size = match.group('size')
                nginx_log_entry = NginxLogEntry(
                    ip_address=match.group('ip'),
                    date_time=date_time,
                    http_method=match.group('method'),
                    url=match.group('url'),
                    response_code=int(match.group('status_code')),
                    response_size=int(size) if size != '-' else 0,
                )
                entries.append(nginx_log_entry)
                print(f'Добавлена запись: {nginx_log_entry}')
            else:
                print(f'Ошибка парсинга строки: {line}')

        try:
            with transaction.atomic():
                NginxLogEntry.objects.bulk_create(entries)
            self.stdout.write(self.style.SUCCESS(f'Данные успешно загружены: {len(entries)} записей'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при сохранении данных: {e}'))