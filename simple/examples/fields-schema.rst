.. _ex/fields-schema:

fields-schema
=============

:ref:`Основное описание <basic/field-schema>`.

Запрос к заказу без схемы, возвращает все поля в максимально простом виде:

**Request**:

.. sourcecode:: http

    GET /v1/services/orders/569bbf1fad7ac9bc5d57d464 HTTP/1.1
    Accept: application/json
    Content-Type: application/json
    Host: ticketscloud.org
    Authorization: key 0123456789abcdef0123456789abcdef

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json; charset=UTF-8
    Server: nginx
    Transfer-Encoding: chunked

    {
        "created_at": "2016-01-17T13:15:31.324000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "569bbf15ad7ac9bc5d57d462",
        "id": "569bbf1fad7ac9bc5d57d464",
        "number": 152799,
        "org": "569bbf2bad7ac9bc5d57d465",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [
            "569bbf3fad7ac9bc5d57d467"
        ],
        "reserved_till": "2016-01-17T13:25:31.351000+00:00",
        "rules": {
            "5661cc619cb5381d9cd87feb": "5661cc619cb5381d9cd87fe6",
            "5661cce99cb5381d9cd88154": "5661cce89cb5381d9cd8814f",
            "5661ce1b9cb53850eed8729c": "5661ce1b9cb53850eed87297",
            "5661cebb9cb5385800d8571b": "566588d39cb538281eee07f9",
            "5661cfb49cb53850eed877e6": "5661cfb49cb53850eed877e2"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "executed",
        "tickets": [
            "569bbf5ead7ac9bc5d57d468"
        ],
        "updated_at": "2016-01-17T13:15:33.735000+00:00",
        "value": "1050.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "1050.00",
            "nominal": "1050.00"
        },
        "vendor": "569bbf2bad7ac9bc5d57d465"
    }

Запрос со схемой, раскрывающий информацию о билетах в заказе и название мероприятия:

**Request**:

.. sourcecode:: http

    GET /v1/resources/orders/569bbf1fad7ac9bc5d57d464?fields-schema=id,tickets{id,serial,number,seat{row,number}},event{title{text}} HTTP/1.1
    Accept: application/json
    Content-Type: application/json
    Host: ticketscloud.org
    Authorization: key 0123456789abcdef0123456789abcdef

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json; charset=UTF-8
    Server: nginx
    Transfer-Encoding: chunked

    {
        "id": "569bbf1fad7ac9bc5d57d464",
        "event": {
            "title": {
                "text": "Тестовое мероприятие"
            }
        },
        "tickets": [
            {
                "id": "569bbf5ead7ac9bc5d57d468",
                "number": 128533,
                "serial": "PTY",
                "seat": {
                    "row": 5,
                    "number": 13
                }
            }
        ]
    }
