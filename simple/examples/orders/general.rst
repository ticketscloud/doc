Создание и изменение заказа
===========================

.. _ex/orders/tickets:

Запрос на создание заказа одного конкретного билета:

**Request**:

.. sourcecode:: http

    POST /v1/resources/orders HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "event": "56a6253df06c5a059a93802e",
        "tickets": [
            "56a6253df06c5a059a9380aa"
        ]
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a6ae06f06c5a21c393805d",
        "created_at": "2016-01-25T23:21:42.154000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291898,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-25T23:31:42.165000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "executed",
        "tickets": [
            "56a6253df06c5a059a9380aa"
        ],
        "updated_at": "2016-01-25T23:21:42.166000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Запрос на добавление билета с заданным id в заказ:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a6ae06f06c5a21c393805d HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "tickets": [
            "56a6253df06c5a059a9380aa",
            "56a6253df06c5a059a9380a4"
        ]
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a6ae06f06c5a21c393805d",
        "created_at": "2016-01-25T23:21:42.154000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291898,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-25T23:31:42.165000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "executed",
        "tickets": [
            "56a6253df06c5a059a9380a4",
            "56a6253df06c5a059a9380aa"
        ],
        "updated_at": "2016-01-25T23:27:56.776000+00:00",
        "value": "200.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "200.00",
            "nominal": "200.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


.. _ex/orders/random:

Запрос на создание заказа (Заказываем два случайных билета из заданного сета):

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
        "id": "56a6a93ef06c5a21c3938059",
        "created_at": "2016-01-25T23:01:18.612000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291896,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-25T23:11:18.625000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "executed",
        "tickets": [
            "56a6253df06c5a059a9380a0"
        ],
        "updated_at": "2016-01-25T23:01:18.625000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Запрос на изменение ранее созданного заказа (добавление еще одного случайного билета в заказ):

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a6a93ef06c5a21c3938059 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "random": {
            "56a6254bf06c5a059b93800c": 2
        }
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a6a93ef06c5a21c3938059",
        "created_at": "2016-01-25T23:01:18.612000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291896,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-25T23:11:18.625000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "status": "executed",
        "tickets": [
            "56a6253df06c5a059a9380a4",
            "56a6253df06c5a059a9380a0"
        ],
        "updated_at": "2016-01-25T23:05:38.937000+00:00",
        "value": "200.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "200.00",
            "nominal": "200.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }
