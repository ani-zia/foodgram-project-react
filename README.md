# praktikum_new_diplom

Первый этап работы, тестирование работы кода:

### 1. API - Примеры запросов

Запросы к API (с примерами) собраны в файле

```
requests.http
```

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/ani-zia/foodgram-project-react.git
```

```
cd foodgram-project-react
```

2. Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```

```
source venv/bin/activate
```

3. Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Зайти в папку с API и выполнить миграции:
```
cd backend
```

```
python3 manage.py migrate
```

5. Запустить проект:
```
python3 manage.py runserver
```

### 2. Локальное тестирование с фронтом

1. Запустить новый терминал и перейти в папку infra
```
cd frontend
```

2. Запустить фронт локально
```
npm run start
```
