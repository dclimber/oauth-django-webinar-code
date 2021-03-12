# Учебный проект для вебинара про Авторизацию и аутентификацию.
Приложение `auth_server` представляет собой комбо из 
**Авторизационного сервера** для OAuth 2.0 протокола и **Сервера ресурсов**, на
котором хранятся стихи великих поэтов.

## Загрузка изначальных данных
Для загрузки поэтов в базу следует прогнать команду:
`python manage.py loaddata fixtures/poets.json`

Для загрузки стихов:
`python manage.py loaddata fixtures/poems.json`

## Создание приложения
Перейдите по адресу: <url сервера>/o/applications/ и создайте приложение.

В форме укажите:

- Client type: Confidential
- Authorization grant type: Resource owner password-based
- Name: тут, что хотите.

Далее вам нужно в `.env` файле приложения `app_server` указать `Client id` и 
`Client secret`.
