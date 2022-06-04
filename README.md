# Foodgram: «Продуктовый помощник»

Можно публиковать свои рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Технологи
Python 3.8.9, Django 4.0.3, Gunicorn, PostgreSQL

![workflow badge](https://github.com/ani-zia/foodgram-project-react/actions/workflows/main.yml/badge.svg)

Сайт в облаке: http://84.201.180.5/
Вход для админа:
```
a@adm.ru
admin5
```

### 1. Запуск на localhost

1. Клонировать репозиторий и перейти в него в командной строке, запустить сборку:
```
git clone https://github.com/ani-zia/foodgram-project-react.git
```

```
cd foodgram-project-react
```

2. Создать и активировать виртуальное окружениеЖ

```
python3 -m venv venv
```

```
source venv/bin/activate
```

3. Шаблон .env файла (значения можно применить из default в файле settings.py):

```
DB_ENGINE=
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
```

4. Собрать и запустить dev-проект в контейнерах

```
cd infra
```

```
docker-compose -f docker-compose.dev.yml up -d --build
```
Команды миграции данных выполняются при сборке.

5. Создать суперпользователя

```
docker-compose exec backend python manage.py createsuperuser
```

6. Ссылки для проверки:

http://localhost/

http://localhost/admin

http://localhost/api/docs/
