FROM python:3.8.5-slim

ENV DB_NAME 'yamdb'
ENV POSTGRES_USER '736od0-postgres'
ENV POSTGRES_PASSWORD 'kd835ek93epostgres'

WORKDIR /app

COPY ../ .

RUN pip3 install -r requirements.txt

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000