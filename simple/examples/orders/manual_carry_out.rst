.. _ex/orders/manual:

Ручное подтверждение заказа
==================

Отправляем запрос на создание заказа:

**Request**:

.. sourcecode:: http

    POST /v1/resources/orders HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
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
        "id": "56a76c72f06c5a77b5938010",
        "created_at": "2016-01-26T12:54:10.744000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291907,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-26T13:04:10.757000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "executed",
        "tickets": [
            "56a6253df06c5a059a9380a0"
        ],
        "updated_at": "2016-01-26T12:54:10.758000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Устанавливаем статус in_progress и платежную систему api/BASE:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a76c72f06c5a77b5938010 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "payment": {
            "system": "api/BASE"
        },
        "status": "in_progress"
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a76c72f06c5a77b5938010",
        "created_at": "2016-01-26T12:54:10.744000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291907,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": "554b31d49cb538549d038eb4"
        },
        "promocodes": [],
        "reserved_till": "2016-01-27T00:57:27.789000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "in_progress",
        "tickets": [
            "56a6253df06c5a059a9380a0"
        ],
        "updated_at": "2016-01-26T12:57:27.789000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Делаем запрос на перевод заказа в статус done и тем самым подтверждаем его оплату:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a76c72f06c5a77b5938010 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "status": "done"
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a76c72f06c5a77b5938010",
        "created_at": "2016-01-26T12:54:10.744000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291907,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": "554b31d49cb538549d038eb4"
        },
        "promocodes": [],
        "reserved_till": "2016-01-27T00:57:27.789000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "done",
        "tickets": [
            "56a6253df06c5a059a9380a0"
        ],
        "updated_at": "2016-01-26T12:57:27.789000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }
