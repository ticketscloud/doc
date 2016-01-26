.. _ex/orders/carry_out:

Запрос на создание заказа с одним слуайным билетом из заданного сета:

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
        "id": "56a73b7ff06c5a21c393806b",
        "created_at": "2016-01-26T09:25:19.378000+00:00", 
        "customer": {
            "lang": "ru"
        }, 
        "deal": null, 
        "event": "56a6253df06c5a059a93802e",  
        "number": 497291903, 
        "org": "56810047f06c5a6ac62f4e1d", 
        "payment": {
            "failure_url": null, 
            "success_url": null, 
            "system": null
        }, 
        "promocodes": [], 
        "reserved_till": "2016-01-26T09:35:19.392000+00:00", 
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
            "56a6253df06c5a059a9380a0"
        ], 
        "updated_at": "2016-01-26T09:25:19.393000+00:00", 
        "value": "100.00", 
        "value_extra": "0.00", 
        "values": {
            "extra": "0.00", 
            "full": "100.00", 
            "nominal": "100.00"
        }, 
        "vendor": "56810047f06c5a6ac62f4e1d"
    }


Запрос на указание платежной системы:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a73b7ff06c5a21c393806b HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json

    {
        "payment": {
            "system": "platron/TEST"
        }
    }

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    {
        "id": "56a73b7ff06c5a21c393806b",
        "created_at": "2016-01-26T09:25:19.378000+00:00", 
        "customer": {
            "lang": "ru"
        }, 
        "deal": null, 
        "event": "56a6253df06c5a059a93802e",  
        "number": 497291903, 
        "org": "56810047f06c5a6ac62f4e1d", 
        "payment": {
            "failure_url": null, 
            "success_url": null, 
            "system": null
        }, 
        "promocodes": [], 
        "reserved_till": "2016-01-26T09:35:19.392000+00:00", 
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
            "56a6253df06c5a059a9380a0"
        ], 
        "updated_at": "2016-01-26T09:25:19.393000+00:00", 
        "value": "100.00", 
        "value_extra": "0.00", 
        "values": {
            "extra": "0.00", 
            "full": "100.00", 
            "nominal": "100.00"
        }, 
        "vendor": "56810047f06c5a6ac62f4e1d"
    }



Запрос на изменение статуса заказа в in_progress:

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/orders/56a73b7ff06c5a21c393806b HTTP/1.1
    Host: api.ticketscloud.org
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
        "created_at": "2016-01-26T09:25:19.378000+00:00", 
        "customer": {
            "lang": "ru"
        }, 
        "deal": null, 
        "event": "56a6253df06c5a059a93802e", 
        "id": "56a73b7ff06c5a21c393806b", 
        "number": 497291903, 
        "org": "56810047f06c5a6ac62f4e1d", 
        "payment": {
            "failure_url": null, 
            "redirect_url": "https://www.platron.ru/payment_params.php?customer=b6cbe4bd8a338159bdf0f4b059652f7023330898", 
            "success_url": null, 
            "system": "545b544a5d645a463e779d53"
        }, 
        "promocodes": [], 
        "reserved_till": "2016-01-26T09:56:06.619000+00:00", 
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
            "56a6253df06c5a059a9380a0"
        ], 
        "updated_at": "2016-01-26T09:26:06.620000+00:00", 
        "value": "100.00", 
        "value_extra": "0.00", 
        "values": {
            "extra": "0.00", 
            "full": "100.00", 
            "nominal": "100.00"
        }, 
        "vendor": "56810047f06c5a6ac62f4e1d"
    }
