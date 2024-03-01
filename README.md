## Приложение "HARDQ"

Платформа для организации обучения студентов с группами,
уроками и доступами + API для получения некоторой информации.

## Что можно сделать в приложении:

- Добавить продукт;
- Добавить студентов;
- Добавить учителей;
- Добавить уроки к продуктам;
- Добавить студентов в группы;
- Распределить студентов по группам примерно равномерно;
- Выдать доступы студентам к продуктам;
- Посмтреть заполненность групп в процентах (api - http://127.0.0.1:8000/api/average_number_in_percentage/)
- Посмотреть инфо о продуктах (сам продукт, количество уроков в продукте и количество студентов с доступом к продукту,)
  api http://127.0.0.1:8000/api/products/)
- Посмотреть список уроков у студента по конкретному продукту по id студента (api http://127.0.0.1:8000/api/lessons/?user_id=1)

## На чем сделано:
- python '3.10.9';
- django '5.0.2';
- BD: litesql.

## Установка:
- `pip install django`
- `pip install djangorestframework`
- `pip install pytz`

## Установка:
- аккаунт админа:
`Admin`
`1234`
