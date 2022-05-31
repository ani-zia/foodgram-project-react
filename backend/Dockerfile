FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . ./

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]