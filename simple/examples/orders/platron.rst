.. _ex/orders/platron:

Работа с платроном
==================

Делаем запрос на создание заказа:

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
        "id": "56a7647cf06c5a28629386a5",
        "created_at": "2016-01-26T12:20:12.707000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291906,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-26T12:30:12.720000+00:00",
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
            "56a6253df06c5a059a9380aa"
        ],
        "updated_at": "2016-01-26T12:20:12.720000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }

Задаем платежную систему, статус in_progress, адреса перехода пользователя при успешной оплате и при неудачной оплате:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a7647cf06c5a28629386a5 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "payment": {
            "failure_url": "http://super-tickets.com/fail",
            "success_url": "http://super-tickets.com/success",
            "system": "platron/TEST"
        },
        "status": "in_progress"
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "created_at": "2016-01-26T12:20:12.707000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "id": "56a7647cf06c5a28629386a5",
        "number": 497291906,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": "http://super-tickets.com/fail",
            "redirect_url": "https://www.platron.ru/payment_params.php?customer=da02cfdd0944f19e3bb75d35d31a7a5623335334",
            "success_url": "http://super-tickets.com/success",
            "system": "545b544a5d645a463e779d53"
        },
        "promocodes": [],
        "reserved_till": "2016-01-26T12:54:33.817000+00:00",
        "rules": {
            "56a6254bf06c5a059b93800c": "56a6254bf06c5a059b93800b"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "in_progress",
        "tickets": [
            "56a6253df06c5a059a9380aa"
        ],
        "updated_at": "2016-01-26T12:24:33.818000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }

После успешной оплаты система перенапрвит пользователя на страницу http://super-tickets.com/success , а статус заказа будет изменен на done.
В случае если оплата не пройдет, пользователя перенаправит на http://super-tickets.com/fail .
