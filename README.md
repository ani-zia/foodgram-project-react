# praktikum_new_diplom

Первый этап работы, тестирование работы кода:

### 1. API - Примеры запросов

Запросы к API (с примерами) собраны в файле

```
requests.http
```

### 2. Запуск на localhost

1. Клонировать репозиторий и перейти в него в командной строке, запустить сборку:
```
git clone https://github.com/ani-zia/foodgram-project-react.git
```

```
cd foodgram-project-react/infra
```

```
docker-compose up -d --build
```
Команды миграции данных выполняются при сборке.

2. Создать суперпользователя

```
docker-compose exec backend python manage.py createsuperuser
```

3. Ссылки для проверки:
http://localhost/
http://localhost/admin
http://localhost/api/docs/