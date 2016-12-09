.. _simple/tickets_info:

Получение информации по билетам
===============================

Для получения информации по билетам связанным с конкретным заказом нужно
сделать запрос ``GET /v1/resources/orders/:id/tickets``

На выходе получаем массив объектов со следующими полями:

:id: id билета
:barcode: штрихкод билета`
:number: номер билета
:serial: серия билета
:seat: место (включает в себя подобъект с рядом, номером места и id сектора)
:set: id квоты в которой находиться билет


Пример использования
======
Имеем:

:API-ключ: `113211f9c3082bbdb29dae7cda1eaf242b`
:ID заказа: `5829c30ad152860018a378b2`

Получаем информацию по билетам заказа:
**Request**:

.. sourcecode:: http

    GET /v1/resources/orders/5829c30ad152860018a378b2/tickets HTTP/1.1
    Host: api.ticketscloud.org
    Accept: */*
    Authorization: key 113211f9c3082bbdb29dae7cda1eaf242b

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: fa310da89cb5387ecf647810

    [
        {
            "id": "582cc243235e3431252b1572",
            "barcode": "60018146012573969",
            "number": 151553,
            "seat": {
                "number": 27,
                "row": 12,
                "sector": "5592c3459cb538014c3a7a36"
            },
            "serial": "AKT",
            "set": "582cc78e515e3500142b128d"
        },
        {
        "id": "582cc291515234560152b1571",
            "barcode": "2572487563832285",
            "number": 151552,
            "seat": {
                "number": 26,
                "row": 12,
                "sector": "5592c3459cb538014c3a7a36"
            },
            "serial": "AKT",
            "set": "582cc78e515e3500142b128d"
        }
    ]
