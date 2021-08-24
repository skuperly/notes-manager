# notes-manager

## Installation

1. Clone this repository: `git clone git@github.com:skuperly/notes-manager.git`.
2. `cd` into `notes-manager`.
3. Install [pipenv](https://github.com/pypa/pipenv).
4. Run `pipenv install`
5. Add `.env` file with environment variables `DEBUG=on` or change it on `settings.py` file.
6. Run `pipenv run python manage.py runserver`.
7. The server start to run on `http://127.0.0.1:8000/`.

## Public Api Endpoints

1. `api/auth/register`, `POST`, `{ username, email, password }`
2. `api/auth/login`, `POST`, `{ username, password }`

## Private Api Endpoints

Requires Header `Authorization: Token xxxxxxx`

1. `api/auth/logout`, `POST`
2. `api/auth/user`, `GET`
3. `api/notes/`, `GET`
4. `api/notes/`, `POST`, `{ title, body }`
5. `api/notes/{id}/`, `PUT`, `{ title, body }`
6. `api/notes/{id}/`, `DELETE`
