# yamdb_final

[![CI](https://github.com/arseniy77/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/arseniy77/yamdb_final/actions/workflows/yamdb_workflow.yml)

## Description 
The YaMDb project collects user reviews of Titles. The works are divided into categories: "Books", "Films", "Music".
The works themselves are not stored in YaMDb, you cannot watch a movie or listen to music here.

## .env-файл с настройками
Внимание! Для запуска контейнера необходимо наличие файла infra/.env с настройками:


ALLOWED_HOSTS = '127.0.0.1,web' #разрешенные имена хостов. Разделитель - запятая.

SECRET_KEY = '<ключ>' #secret-key Django

DB_ENGINE = 'django.db.backends.postgresql'

DB_NAME = '<имя>' #имя базы данных

POSTGRES_USER = '<username>' #Имя пользователя базы данных

POSTGRES_PASSWORD = '<пароль>' #пароль базы данных

DB_HOST = 'db' #Имя хоста базы данных

DB_PORT = <порт> #Порт базы данных

## Для запуска:
1. После запуска контейнера Docker-Compose, выполните команды для первоначальной настройки:

`docker-compose exec web chmod +x ./startup.sh`

`docker-compose exec -it web ./startup.sh`


2. После приглашения, введите данные учетной записи суперпользователя
3. Доступ в панель админимтратора возможен по адресу [sitename/admin/](http://127.0.0.1/admin/)

    Например: [http://127.0.0.1/admin/](http://127.0.0.1/admin/)
4. Если у вас есть файл с дампом базы данных, вы можете загрузить свою базу с помощью команды:

    `docker-compose exec python manage.py loaddata <имя файла>`


## Ednpoints
api/v1/auth/signup/ - Post request, Register (Using 'me' as username is prohibited.)
***
api/v1/auth/token/ - Post request, Obtaining a JWT token in exchange for a username and confirmation code
***
api/v1/categories/ - Get request, getting a list of categories
***
api/v1/genres/ - Get request, get a list of all genres
***
api/v1/titles/ - Get request, getting a list of all works
***
api/v1/titles/{titles_id}/ - Get request, getting information about the titles
***
api/v1/titles/{title_id}/reviews/ - Get request, get a list of all reviews
***
api/v1/titles/{title_id}/reviews/ - Post request, adding a new review
***
api/v1/titles/{title_id}/reviews/{review_id}/ - Get request, getting a response by id
***
api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Get request, get a list of all review comments
***
api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Post request, adding a comment to a review
***
api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Get request, get a comment on a review

## Authors
Андрей Антонов
Арсений Гаинцев 
Егор Графов

## License
You may copy, distribute and modify the software as long as you track changes/dates in source files. Any modifications to or software including (via compiler) GPL-licensed code must also be made available under the GPL along with build & install instructions.
