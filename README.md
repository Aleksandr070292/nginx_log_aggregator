# Nginx Log Aggregator

## Описание

Этот проект представляет собой Django приложение для обработки и агрегации логов Nginx. Приложение включает в себя management команду для загрузки лог-файла, его парсинга и сохранения данных в базу данных. Данные можно просматривать и фильтровать через Django Admin и REST API, реализованный с помощью Django REST Framework (DRF).

## Возможности

- Парсинг и сохранение логов Nginx в базу данных.
- Отображение загруженных данных через Django Admin.
- REST API для доступа к данным с поддержкой пагинации, фильтров и поиска.
- Документация API с помощью Swagger (drf-yasg).
- Запуск проекта в контейнерах Docker с использованием Docker Compose.
- Тесты для проверки корректности работы.

## Требования

- Python 3.11
- Django >= 4.2
- Sqlite3
- Docker и Docker Compose

## Установка и настройка

1. Клонируйте репозиторий:
    ```bash
    git clone <ссылка на репозиторий>
    cd nginx_log_aggregator
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Выполните миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Использование

### Импорт логов

Для импорта лог-файлов используйте management команду:

```bash
python manage.py import_nginx_log <URL>