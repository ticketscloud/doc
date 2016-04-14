.. _ex/orders/promocodes:

Использование промокодов
========================

Делаем запрос на создание заказа:

**Request**:

.. sourcecode:: http

    POST /v1/resources/orders HTTP/1.1
    Accept: application/json
    Accept-Encoding: gzip, deflate
    Authorization:  key 769313917cb94710860b507323134796
    Connection: keep-alive
    Content-Length: 80
    Content-Type: application/json
    Host: stage.ticketscloud.org
    User-Agent: HTTPie/0.9.3

    {
        "event": "570fb4f62d70951b3a2b0b5c",
        "random": {
            "570fb5082d70951b372b0b7b": 3
        }
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 201 Created
    Cache-Control: private, max-age=0, no-cache, no-store
    Connection: keep-alive
    Content-Length: 860
    Content-Type: application/json; charset=UTF-8
    Date: Thu, 14 Apr 2016 15:26:45 GMT
    Server: nginx/1.6.2
    X-Partner: 570faa682d70951b372b0b56

    {
        "created_at": "2016-04-14T15:26:45.664000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "570fb4f62d70951b3a2b0b5c",
        "id": "570fb6b52d70951b392b0f35",
        "number": 220994,
        "org": "570faa682d70951b372b0b56",
        "payment": {
            "system": null
        },
        "promocodes": [],
        "reserved_till": "2016-04-14T15:36:45.688000+00:00",
        "rules": {
            "570fb5082d70951b372b0b7b": "570fb5082d70951b372b0b7a"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "executed",
        "tickets": [
            "570fb5082d709579c102b556",
            "570fb5082d709579c102b554",
            "570fb5082d709579c102b555"
        ],
        "updated_at": "2016-04-14T15:26:45.688000+00:00",
        "value": "300.00",
        "value_extra": "0.00",
        "values": {
            "discount": "0.00",
            "extra": "0.00",
            "full": "300.00",
            "nominal": "300.00",
            "sets": [
                {
                    "d": "0.00",
                    "id": "570fb5082d70951b372b0b7b",
                    "p": "100.00",
                    "ps": []
                }
            ]
        },
        "vendor": "570faa682d70951b372b0b56"
    }

Применяем ранее созданный промокод на 30% "PROMO" к заказу

**Request**

.. sourcecode:: http

    PATCH /v1/resources/orders/570fb6b52d70951b392b0f35 HTTP/1.1
    Accept: application/json
    Accept-Encoding: gzip, deflate
    Authorization:  key 769313917cb94710860b507323134796
    Connection: keep-alive
    Content-Length: 25
    Content-Type: application/json
    Host: stage.ticketscloud.org
    User-Agent: HTTPie/0.9.3

    {
        "promocodes": [
            "PROMO"
        ]
    }

**Response**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Cache-Control: private, max-age=0, no-cache, no-store
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json; charset=UTF-8
    Date: Thu, 14 Apr 2016 15:35:26 GMT
    Server: nginx/1.6.2
    Transfer-Encoding: chunked
    X-Partner: 570faa682d70951b372b0b56

    {
        "created_at": "2016-04-14T15:26:45.664000+00:00",
        "customer": {
            "lang": "ru"
        },
        "deal": null,
        "event": "570fb4f62d70951b3a2b0b5c",
        "id": "570fb6b52d70951b392b0f35",
        "number": 220994,
        "org": "570faa682d70951b372b0b56",
        "payment": {
            "system": null
        },
        "promocodes": [
            "570fb8952d70951b382b0b65"
        ],
        "reserved_till": "2016-04-14T15:36:45.688000+00:00",
        "rules": {
            "570fb5082d70951b372b0b7b": "570fb5082d70951b372b0b7a"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "executed",
        "tickets": [
            "570fb5082d709579c102b556",
            "570fb5082d709579c102b554",
            "570fb5082d709579c102b555"
        ],
        "updated_at": "2016-04-14T15:35:26.046000+00:00",
        "value": "210.00",
        "value_extra": "0.00",
        "values": {
            "discount": "90.00",
            "extra": "0.00",
            "full": "210.00",
            "nominal": "210.00",
            "sets": [
                {
                    "d": "30.00",
                    "id": "570fb5082d70951b372b0b7b",
                    "p": "70.00",
                    "ps": [
                        "570fb8952d70951b382b0b65"
                    ]
                }
            ]
        },
        "vendor": "570faa682d70951b372b0b56"
    }

В результате успешного применения промокода цены в разделе "values"
изменились и в массиве promocodes появился новый элемент.
