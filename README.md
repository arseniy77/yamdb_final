# yamdb_final

[![CI](https://github.com/arseniy77/yamdb_final/actions/workflows/main.yml/badge.svg)](https://github.com/arseniy77/yamdb_final/actions/workflows/main.yml)

## Description 
The YaMDb project collects user reviews of Titles. The works are divided into categories: "Books", "Films", "Music".
The works themselves are not stored in YaMDb, you cannot watch a movie or listen to music here.

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
