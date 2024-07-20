# Library Management System

## Описание

Это консольное приложение для управления библиотекой книг, разработанное с использованием Django REST Framework и PostgreSQL. Оно позволяет добавлять, удалять, искать и отображать книги. Каждая книга имеет следующие поля:

- `id`: Уникальный идентификатор (генерируется автоматически)
- `title`: Название книги
- `author`: Автор книги
- `year`: Год издания
- `status`: Статус книги ("в наличии" или "выдана")

## Функциональность

- **Добавление книги**: Введите `title`, `author` и `year`, после чего книга будет добавлена в библиотеку с уникальным `id` и статусом "в наличии".
- **Удаление книги**: Введите `id` книги для её удаления.
- **Поиск книги**: Введите `title`, `author` или `year` для поиска книги.
- **Отображение всех книг**: Выводит список всех книг с их `id`, `title`, `author`, `year` и `status`.
- **Изменение статуса книги**: Введите `id` книги и новый статус ("в наличии" или "выдана").

## Установка и настройка

### Предварительные требования

- Python 3.6+
- PostgreSQL

### Шаги установки

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your_username/library_management.git
    cd library_management
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Настройте базу данных PostgreSQL в `library_management/settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'library_db',
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Примените миграции:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

### Использование

Для выполнения операций с книгами используйте следующие команды:

- **Добавление книги**:

    ```bash
    python manage.py library_console add
    ```

- **Удаление книги**:

    ```bash
    python manage.py library_console delete
    ```

- **Поиск книги**:

    ```bash
    python manage.py library_console search
    ```

- **Отображение всех книг**:

    ```bash
    python manage.py library_console list
    ```

- **Изменение статуса книги**:

    ```bash
    python manage.py library_console update_status
    ```

### Тестирование

Для запуска тестов используйте команду:

```bash
python manage.py test
