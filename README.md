# Book Info Uploader

Это Django приложение, которое позволяет пользователям загружать книги в форматах EPUB и FB2, а затем анализирует метаданные книг и выводит- Название книги, имя автора, название издательства, год издания и сохраняет их в базе данных.

## Установка и настройка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/talasov/Parserbook.git
    cd Parserbook
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

## Запуск приложения

1. Запустите локальный сервер:

    ```bash
    python manage.py runserver
    ```

2. Откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000/upload/

3. Загрузите файл в формате EPUB или FB2 с метаданными о книге.

4. Выведуться данные.
###### пример: 
```commandline
Book Information
Title: Мастер и Маргарита

Author: Булгаков Михаил Афанасьевич

Publisher: Эксмо

Year: 2006

© 2023 BookParser
```


## Запуск скрипта для анализа ID

1. Запустите скрипт для анализа ID:

В директории BookParser/scripts, запустить файл data_analysis_scripts.py

Скрипт анализирует ID в файле, выводит ID, которые встречаются 3 раза, и частоту повторений.

## Зависимости

- Django
- ebooklib
- beautifulsoup4
- pandas


