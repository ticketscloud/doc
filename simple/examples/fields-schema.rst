.. _ex/fields-schema:

fields-schema
=============

:ref:`Основное описание <basic/field-schema>`.

Запрос к заказу без схемы, возвращает все поля в максимально простом виде:

**Request**:

.. sourcecode:: http

   GET /v1/resources/orders/56a69feaf06c5a21c3938057 HTTP/1.1
   Host: api.ticketscloud.org
   Accept: application/json
   Authorization:  key 047bdb8bcee44d3693371920aaf9135c
   Content-Type: application/json

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a69feaf06c5a21c3938057",
        "created_at": "2016-01-25T22:21:30.737000+00:00",
        "customer": {
            "email": "volkov@alex.com",
            "first_name": "Алексей",
            "lang": null,
            "last_name": "Волков",
            "mobile": "89167683232",
            "user": "56a6a01841226dbf3b346180"
        },
        "deal": null,
        "event": "568a22b5f06c5a42975fb913",
        "number": 497291895,
        "org": "56810047f06c5a6ac62f4e1d",
        "payment": {
            "failure_url": "http://ticketscloud.org/",
            "redirect_url": "https://www.goodservice.ru/ps/test/start_payment.php?payment_id=23324826",
            "success_url": "http://ticketscloud.org/?tcordersuccess=497291895",
            "system": "545b544a5d645a463e779d53"
        },
        "promocodes": [],
        "reserved_till": "2016-01-25T22:52:21.062000+00:00",
        "rules": {
            "568a22b6f06c5a42985fb914": "56a61828f06c5a059b937fdc"
        },
        "status": "in_progress",
        "tickets": [
            "568a22b6f06c5a42e8847c55"
        ],
        "updated_at": "2016-01-25T22:22:21.063000+00:00",
        "value": "100.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "100.00",
            "nominal": "100.00"
        },
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Запрос со схемой, раскрывающий информацию о билетах в заказе и название мероприятия:

**Request**:

.. sourcecode:: http

   GET /v1/resources/orders/56a69feaf06c5a21c3938057?fields-schema=id,tickets%7Bid,serial,number,seat%7Brow,number%7D%7D,event%7Btitle%7Btext%7D%7D HTTP/1.1
   Host: ticketscloud.org
   Accept: application/json
   Authorization:  key 047bdb8bcee44d3693371920aaf9135c
   Content-Type: application/json

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a69feaf06c5a21c3938057",
        "event": {
            "title": {
                "text": "test"
            }
        },
        "tickets": [
            {
                "id": "568a22b6f06c5a42e8847c55",
                "number": 118398,
                "seat": {},
                "serial": "AEY"
            }
        ]
    }
