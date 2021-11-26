FROM ubuntu

WORKDIR /app

COPY ../ .

RUN pip3 install -r requirements.txt

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000