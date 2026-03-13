# Skystore

Учебный проект интернет-магазина, разработанный в рамках курса по Django.

## Описание

Skystore — веб-приложение на Django с каталогом продуктов, страницей контактов и формой обратной связи.

## Технологии

- Python 3.13
- Django 6.0
- PostgreSQL
- Bootstrap 5
- Poetry

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone <ссылка на репозиторий>
cd django-22
```

2. Установите зависимости через Poetry:
```bash
poetry install --no-root
```

3. Активируйте виртуальное окружение:
```bash
poetry env activate
```

4. Создайте файл `.env` в корне проекта:
```
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
DB_NAME=имя_базы_данных
DB_USER=postgres
DB_PASSWORD=ваш_пароль
DB_HOST=localhost
DB_PORT=5432
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Запустите сервер:
```bash
python manage.py runserver
```

7. Откройте в браузере: http://127.0.0.1:8000/

## Структура проекта

```
django-22/
├── catalog/          # Приложение каталога
│   ├── templates/    # HTML шаблоны
│   ├── views.py      # Контроллеры
│   └── urls.py       # Маршруты
├── config/           # Настройки проекта
├── static/           # Статические файлы
├── .env              # Переменные окружения (не в git)
├── .gitignore
└── manage.py
```

## Страницы

- `/` — Главная страница
- `/contacts/` — Страница контактов с формой обратной связи