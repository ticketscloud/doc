.. _ex/invitation:

Отправка пригласительных
========================

Процедура аналогична простому :ref:`созданию заказа <simple/orders/create>`,
но в отличии от обычного заказа
требуется :ref:`установить значение платежной системы <simple/orders/ps>`
в ``system/INVITATION``

Создаем заказ:

**Request**:

.. sourcecode:: http

    POST /v1/resources/orders HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 4ac74fac981642499859fc2148542f40
    Content-Type: application/json

    {
        "customer": {
            "email": "test@gmail.com"
        },
        "event": "56ec0b0b2d70951a00fffd12",
        "payment": {
            "system": "system/INVITATION"
        },
        "random": {
            "56ec0b342d70951a00fffd14": 2
        }
    }


**Response**:

.. sourcecode:: http

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56ec0ad62d70951a00fffd10

    {
        "created_at": "2016-03-18T15:47:20.772000+00:00",
        "customer": {
            "email": "test@gmail.com",
            "first_name": null,
            "lang": null,
            "last_name": null,
            "mobile": null,
            "user": "555c97ea9cb53866d2a19851"
        },
        "deal": null,
        "event": "56ec0b0b2d70951a00fffd12",
        "id": "56ec23082d70951a01fffd2b",
        "number": 202477,
        "org": "56ec0ad62d70951a00fffd10",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": "553a6ad49cb538165c3a6ad9"
        },
        "promocodes": [],
        "reserved_till": "2016-03-18T15:57:20.789000+00:00",
        "rules": {
            "56ec0b342d70951a00fffd14": "56ec0c402d70951a01fffd22"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "executed",
        "tickets": [
            "56ec0b342d70951a3da28713",
            "56ec0b342d70951a3da28712"
        ],
        "updated_at": "2016-03-18T15:47:20.789000+00:00",
        "value": "180.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "180.00",
            "nominal": "180.00"
        },
        "vendor": "56ec0ad62d70951a00fffd10"
    }

После того как заказ успешно созда переводим его в статус :ref:`in_progress`:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56ec23082d70951a01fffd2b HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 4ac74fac981642499859fc2148542f40
    Content-Type: application/json

    {
        "status": "in_progress"
    }


**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56ec0ad62d70951a00fffd10

    {
        "created_at": "2016-03-18T15:47:20.772000+00:00",
        "customer": {
            "email": "test@gmail.com",
            "first_name": null,
            "lang": null,
            "last_name": null,
            "mobile": null,
            "user": "555c97ea9cb53866d2a19851"
        },
        "deal": null,
        "event": "56ec0b0b2d70951a00fffd12",
        "id": "56ec23082d70951a01fffd2b",
        "number": 202477,
        "org": "56ec0ad62d70951a00fffd10",
        "payment": {
            "failure_url": null,
            "success_url": null,
            "system": "553a6ad49cb538165c3a6ad9"
        },
        "promocodes": [],
        "reserved_till": "2016-03-18T15:57:20.789000+00:00",
        "rules": {
            "56ec0b342d70951a00fffd14": "56ec0c402d70951a01fffd22"
        },
        "salespoint": {
            "blanks": {
                "rejected": {},
                "used": {}
            }
        },
        "status": "done",
        "tickets": [
            "56ec0b342d70951a3da28713",
            "56ec0b342d70951a3da28712"
        ],
        "updated_at": "2016-03-18T15:48:51.351000+00:00",
        "value": "0.00",
        "value_extra": "0.00",
        "values": {
            "extra": "0.00",
            "full": "180.00",
            "nominal": "180.00"
        },
        "vendor": "56ec0ad62d70951a00fffd10"
    }

После перевода заказа в статус :ref:`in_progress` система автоматически
переведет его в статус ``done`` и билеты будут высланы на указанный адрес.
