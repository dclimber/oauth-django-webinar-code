# Учебный проект для вебинара «Аутентификация, Авторизация, хранение секретов».
## Описание
1. В папке `app_server` находится **«Клиент»**.
   - Для переменных окружения использует библиотеку [decouple](https://github.com/henriquebastos/python-decouple)
2. В папке `auth_server` находятся **«сервер-ресурсов»** и **«сервер-авторизации»**:
   1. Сервер ресурсов реализован приложением `poems`, представляет собой
      базу данных с со стихами Великих поэтов и поэтэсс.
      - API-ресурсов использует [django-rest-framework](https://www.django-rest-framework.org/), тема следующего спринта.
      - Для вьюх моделей используется [ModelViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)
   1. Сервер авторизации реализован на библиотеке [Django OAuth Toolkit](https://github.com/jazzband/django-oauth-toolkit)
   2. Для переменных окружения использует библиотеку [django-environ](https://github.com/joke2k/django-environ)

## Инструкция по настройке/установке
1. Создайте виртуальное окружение, назовите папку `env`
2. Установите зависимости из `requirements.txt`
3. Заполните файлы переменных окружения `.env` в обоих проектах.
   Для этого:
   1) Создайте файл `.env` рядом с файлом `.env.template`;
   2) Скопируйте содержимое файла `.env.template` в файл `.env`;
   3) Заполните значения в файлах.
   4) В `app_server` значения:
      1) `OAUTH_SERVER_URL` должно быть `http://127.0.0.1:8001`
      2) `CLIENT_ID` и `CLIENT_SECRET` мы заполним на вебинаре.
4. Сделайте миграции в `auth_server` и `app_server`.
5. Загрузите [фикстуры](https://docs.djangoproject.com/en/3.1/howto/initial-data/) в `auth_server`:
   1. Для загрузки поэтов в базу следует прогнать команду:
      
      ```python manage.py loaddata fixtures/poets.json```
   
   2. Для загрузки стихов:
      
      ```python manage.py loaddata fixtures/poems.json```

6. Создайте «супер пользователя» на сервере ресурсов.
7. Запустите сервер ресурсов и авторизации: 
   
   ```python manage.py runserver 0.0.0.0:8001```

8.  Откройте [сервер-ресурсов](http://127.0.0.1:8001/) в браузере.
9.  Запустите приложение-клиента: 
   
    ```python manage.py runserver 0.0.0.0:8002```

10. Откройте [приложение-клиента](http://127.0.0.1:8002/) в браузере.

### Создание приложения
1. Перейдите по адресу: [<url сервера авторизации>/o/applications/](http://127.0.0.1:8001/o/applications/)) и создайте приложение.
2. В форме укажите:
   - Client type: `Confidential`
   - Authorization grant type: `Authorization code`
   - Name: тут, что хотите.
   - Redirect uris: `http://127.0.0.1:8002/callback/`
3. Далее вам нужно в `.env` файле приложения `app_server` указать:
   1) `CLIENT_ID`
   2) `CLIENT_SECRET`
