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
        "id": "56a8bcaff06c5a7618650402",
        "created_at": "2016-01-27T12:48:47.897000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291925,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-01-27T12:58:47.911000+00:00",
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
        "updated_at": "2016-01-27T12:48:47.912000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Задаем платежную систему, адреса перехода пользователя при успешной оплате и при неудачной оплате,
а так же информацию о покупателе, его имя, фамилию и email:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a8bcaff06c5a7618650402 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "customer": {
            "email": "volkov@email.org",
            "first_name": "Алексей",
            "last_name": "Волков"
        },
        "payment": {
            "failure_url": "http://super-tickets.com/fail",
            "success_url": "http://super-tickets.com/success",
            "system": "platron/TEST"
        }
    }


**Response**:

.. sourcecode:: http

HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
X-Partner: 56810047f06c5a6ac62f4e1d

{
    "id": "56a8bcaff06c5a7618650402",
    "created_at": "2016-01-27T12:48:47.897000+00:00",
    "customer": {
        "lang": "ru"
    },
    "deal": null,
    "event": "56a6253df06c5a059a93802e",
    "number": 497291925,
    "org": "56810047f06c5a6ac62f4e1d",
    "payment": {
        "failure_url": null,
        "success_url": null,
        "system": null
    },
    "promocodes": [],
    "reserved_till": "2016-01-27T12:58:47.911000+00:00",
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
    "updated_at": "2016-01-27T12:48:47.912000+00:00",
    "value": "100.00",
    "value_extra": "0.00",
    "values": {
        "extra": "0.00",
        "full": "100.00",
        "nominal": "100.00"
    },
    "vendor": "56810047f06c5a6ac62f4e1d"
}


Переводим заказ в статус in_progress:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a8bcaff06c5a7618650402 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

{
    "status": "in_progress"
}


**Response**:

.. sourcecode:: http

   HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a8bcaff06c5a7618650402",
        "created_at": "2016-01-27T12:48:47.897000+00:00",
        "customer": {
            "email": "volkov@email.org",
            "first_name": "Алексей",
            "lang": null,
            "last_name": "Волков",
            "mobile": null,
            "user": "56a8bb6a41226dbf3b346182"
        },
        "deal": null,
        "event": "56a6253df06c5a059a93802e",
        "number": 497291925,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": "http://super-tickets.com/fail",
            "redirect_url": "https://www.platron.ru/payment_params.php?customer=dae1c99051f6cc7302a3bacdb67bf2ce23356852",
            "success_url": "http://super-tickets.com/success",
            "system": "545b544a5d645a463e779d53"
        },
        "promocodes": [],
        "reserved_till": "2016-01-27T13:19:06.074000+00:00",
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
            "56a6253df06c5a059a9380ac"
        ],
        "updated_at": "2016-01-27T12:49:06.074000+00:00",
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
