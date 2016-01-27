.. _ex/orders/all_or_nothing:

Флаг ``all_or_nothing``
=============

В сете находятся 3 свободных билета.

Отправляем запрос на создание заказа с 2-мя билетами:

**Request**:

.. sourcecode:: http

    POST /v1/resources/orders HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "all_or_nothing": "true",
        "event": "56a6253df06c5a059a93802e",
        "random": {
            "56a6254bf06c5a059b93800c": 2
        }
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a774a8f06c5a28629386b8",
        "created_at": "2016-01-26T13:29:12.624000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291912,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-26T13:39:12.642000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "executed",
        "tickets": [
            "56a6253df06c5a059a9380ae",
            "56a6253df06c5a059a9380b0"
        ],
        "updated_at": "2016-01-26T13:29:12.642000+00:00",
        "value": "200.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "200.00",
            "nominal": "200.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }

Нам удалось забронировать два билета.

Отправляем еще один запрос на создание заказа c двумя билетами:

**Request**:

.. sourcecode:: http

    POST /v1/resources/orders HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "all_or_nothing": "true",
        "event": "56a6253df06c5a059a93802e",
        "random": {
            "56a6254bf06c5a059b93800c": 1
        }
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a7752af06c5a28629386ba",
        "created_at": "2016-01-26T13:31:22.838000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291913,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-26T13:41:22.844000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "executed",
        "tickets": [],
        "updated_at": "2016-01-26T13:31:22.844000+00:00",
        "value": "0.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "0.00",
            "nominal": "0.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }

Второй запрос не вернул ни одного id билета в поле tickets так как остался всего один свободный билет в сете и в запросе присутствовал активный флаг ``all_or_nothing``.
