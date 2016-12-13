.. _simple/user_legal:

========================================
Получение юр. информации об организаторе
========================================

Для получения юридической информации об организаторе мероприятия необходимо
сделать запрос на ``GET /v1/resources/partners/:partner_id?fields-schema=legal{type,bank,detail,who}``


Пример использования
====================

Мы распространитель и у нас есть один оплаченный заказ.
Нам необходимо получить информацию об организаторе.
Имеем:
:API-ключ: `0205be31ef3846d4a163ce71aa6d16b6`
:ID заказа: `584e9ad50944c10017e3a9df`

Получаем id партнрера организатор:

**Request**:

.. sourcecode:: http

    GET /v1/resources/orders/584e9ad50944c10017e3a9df?fields-schema=org HTTP/1.1
    Accept: */*
    Authorization: key 0205be31ef3846d4a163ce71aa6d16b6

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 584e8df10944c1001ae3a9e3

    {
        "org": "584e8bc20944c10017e3a9d3"
    }

Имея идентификатор партнера организатора можем получить его юридическую информацию:
**Request**:

.. sourcecode:: http

    GET /v1/resources/partners/584e8bc20944c10017e3a9d3?fields-schema=legal%7Btype,bank,detail,who%7D HTTP/1.1
    Accept: */*
    Authorization: key 0205be31ef3846d4a163ce71aa6d16b6


**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 584e8df10944c1001ae3a9e3

    {
        "legal": {
            "bank": {
                "bik": "432424234",
                "ks": "42343242342342242424",
                "name": "БанкЪ",
                "rs": "43242423424242334224"
            },
            "detail": {
                "address": "Супер орг",
                "inn": "423423643275",
                "name": "ИП Супер орг",
                "nds": false,
                "ogrnip": "423424234234322",
                "taxes": "osn",
                "type": "ru/ltd"
            },
            "type": "ru/ip",
            "who": {
                "name": "",
                "position": "",
                "reason": "на основании устава"
            }
        }
    }
