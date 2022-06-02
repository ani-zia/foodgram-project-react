# Foodgram: «Продуктовый помощник»

Можно публиковать свои рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

![workflow badge](https://github.com/ani-zia/foodgram-project-react/actions/workflows/main.yml/badge.svg)

Сайт в облаке: http://84.201.180.5/

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

3. Собрать и запустить проект в контейнерах

```
cd infra
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