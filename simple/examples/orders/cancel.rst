.. _ex/orders/cancel:

Отмена заказа
=============

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
        "id": "56a7717ff06c5a28629386b3",
        "created_at": "2016-01-26T13:15:43.289000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291910,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-26T13:25:43.302000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "executed",
        "tickets": [
            "56a6253df06c5a059a9380ac"
        ],
        "updated_at": "2016-01-26T13:15:43.302000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Отправляем запрос на изменение статуса на canceled и тем самым отменяем заказ:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a7717ff06c5a28629386b3 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "status": "canceled"
    }


**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a7717ff06c5a28629386b3",
        "created_at": "2016-01-26T13:15:43.289000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291910,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-26T13:25:43.302000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "canceled",
        "tickets": [
            "56a6253df06c5a059a9380ac"
        ],
        "updated_at": "2016-01-26T13:15:43.302000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }
