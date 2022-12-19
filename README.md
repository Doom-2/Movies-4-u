# Movies-4-U
### Netflix analogue with users support.
### Containerized with Docker, running on Gunicorn. CI/CD integration is used

[movies-4-u.ga](http://movies-4-u.ga)

Features:
- User authentication
- User profile, including password change ability
- Favorites page
- Filtering movies by director and genre

Details:
1. Выполнить файл db_utils/create_tables.py для создания БД и таблиц в ней
2. Выполнить файл db_utils/load_fixtures.py для заполнения некоторых таблиц.
3. Запустить фласк приложение из файла app.py
4. Пользователей можно создавать как через браузер, так и из файла http/test_api.http, первые 3 POST-запроса.
5. Аутентификацию можно делать как через браузер, так и из файла http/auth.http, первые 3 POST-запроса.

Проект работает с frontend стендом на порте 5000 (изменил порт в .js файле, изначально был 25000).
Изменил расположение картинок на static/img и пути к ним в index.html для их отображения в браузере.
Файл manifest.json переложен в папку static, чтобы Flask находил его.
Промежуточные коммиты согласно заданию не делал, упустил этот момент, есть коммит готового проекта.

Тестирование:
Тесты на сервисы написаны.

Не написаны тесты на маршруты, где требуется аутентификация.

Тестирование DAO методов с обращением к БД реализовано частично, создал 3 функции с обращенем к БД и протестировал их через MagicMock.

Доступно по URL:

http://movies-4-u.ga

http://158.160.37.55