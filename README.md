# elecshop

### Модель сети по продаже электроники

Проект на DJANGO+DRF+PostgreSQL<br>
Зависимости в reqierements.txt<br>
Примеры переменных окружения в env_example



#### Создание участника цепи поставок:

POST localhost:8000<br>
    {<br>
    "name": "Some Name",<br>
    "country": "Some Country",<br>
    "city": "Some City",<br>
    "street": "Some Street",<br>
    "building": "1234",<br>
    "debt": "1233.12",<br>
    "supplier": 1,<br>
    "product": 1<br>
    }<br>

#### Просмотр первого участника цепи поставок:
GET localhost:8000/1/<br>

#### Просмотр списка участников цепи поставок:
GET localhost:8000/<br>

#### Изменение первого участника цепи поставок:
PATCH localhost:8000/1/<br>
    {<br>
    "name": "Some New Name"<br>
    }<br>

#### Удаление первого участника цепи поставок:
DELETE localhost:8000/1/<br>
