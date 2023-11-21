# Тестовое задание: Древовидное меню

## Описание:

Разработано приложение на Django, в котором через template tag реализовано древовидное меню.
Через django-админку можно создавать и редактировать меню.
По ендпоинту `/menu/` доступно древовидное меню.

Настройка меню через админку:
1. В админке необходимо создайте объект модели Menu с именем `menu_name`.
2. Создать объекты для MenuItem для создания древовидного меню.
3. После создания по ендпоинту `/menu/` будет доступно древовидное меню.

## Технологии проекта:

- Python 3.11
- Django 4.2.7

## Установка:

Для установки проекта на локальной машине необходимо:

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:alekseikoznov/menu-app.git
```
```
cd menu-app
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас Windows
    ```
    source venv/scripts/activate
    ```
3. Обновить менеджер пакетов pip:
```
python -m pip install --upgrade pip
```
4. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
5. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```
6. В папке с файлом manage.py создайте админа:
```
python manage.py createsuperuser
```
7. В папке с файлом manage.py запустите локальный сервер:
```
python manage.py runserver
```
