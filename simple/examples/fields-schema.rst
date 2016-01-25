.. _ex/fields-schema:

fields-schema
=============

:ref:`Основное описание <basic/field-schema>`.

Запрос к заказу без схемы, возвращает все поля в максимально простом виде:

**Request**:

.. sourcecode:: http

    GET https://ticketscloud.org/v1/resources/orders/56a62942f06c5a059b93800f
    Authorization: key 047bdb8bcee44d3693371920aaf9135c
    Accept: application/json
    Content-Type: application/json

**Response**:

.. sourcecode:: http

    {
      "id": "56a62942f06c5a059b93800f",
      "customer": {
        "lang": null,
        "last_name": "Алексей",
        "first_name": "Волков",
        "user": "56a6296b41226dbf3b34617f",
        "email": "volchek@alex.org",
        "mobile": "89167683232"
      },
      "deal": null,
      "status": "expired",
      "values": {
        "full": "100.00",
        "nominal": "100.00",
        "extra": "0.00"
      },
      "updated_at": "2016-01-25T14:26:12.721000+00:00",
      "rules": {
        "568a22b6f06c5a42985fb914": "56a61828f06c5a059b937fdc"
      },
      "salespoint": {
        "blanks": {
          "used": null,
          "rejected": null
        }
      },
      "created_at": "2016-01-25T13:55:14.220000+00:00",
      "org": "56810047f06c5a6ac62f4e1d",
      "vendor": "56810047f06c5a6ac62f4e1d",
      "reserved_till": null,
      "promocodes": [],
      "value_extra": "0.00",
      "payment": {
        "redirect_url": "https://www.platron.ru/ps/test/start_payment.php?payment_id=23315790",
        "success_url": "http://ticketscloud.org/?tcordersuccess=497291884",
        "failure_url": "http://ticketscloud.org/",
        "system": "545b544a5d645a463e779d53"
      },
      "tickets": [
        "568a22b6f06c5a42e8847c55"
      ],
      "number": 497291884,
      "event": "568a22b5f06c5a42975fb913",
      "value": "100.00"
    }
    // GET https://ticketscloud.org/v1/resources/orders/56a62942f06c5a059b93800f
    // HTTP/1.1 200 OK
    // Server: nginx/1.8.0
    // Date: Mon, 25 Jan 2016 14:31:30 GMT
    // Content-Type: application/json; charset=UTF-8
    // Content-Length: 1104
    // Connection: keep-alive
    // X-Partner: 56810047f06c5a6ac62f4e1d
    // Cache-Control: private, max-age=0, no-cache, no-store
    // Request duration: 0.696011s


Запрос со схемой, раскрывающий информацию о билетах в заказе и название мероприятия:

**Request**:

.. sourcecode:: http

   GET https://ticketscloud.org/v1/resources/orders/56a62942f06c5a059b93800f?fields-schema=id,tickets{id,serial,number,seat{row,number}},event{title{text}}
   Authorization: key 047bdb8bcee44d3693371920aaf9135c
   Accept: application/json
   Content-Type: application/json

**Response**:

.. sourcecode:: http

    {
      "id": "56a62942f06c5a059b93800f",
      "tickets": [
        {
          "serial": "AEY",
          "seat": null,
          "number": 118398,
          "id": "568a22b6f06c5a42e8847c55"
        }
      ],
      "event": {
        "title": {
          "text": "test"
        }
      }
    }
    // GET https://ticketscloud.org/v1/resources/orders/56a62942f06c5a059b93800f?fields-schema=id,tickets{id,serial,number,seat{row,number}},event{title{text}}
    // HTTP/1.1 200 OK
    // Server: nginx/1.8.0
    // Date: Mon, 25 Jan 2016 14:39:11 GMT
    // Content-Type: application/json; charset=UTF-8
    // Content-Length: 168
    // Connection: keep-alive
    // X-Partner: 56810047f06c5a6ac62f4e1d
    // Cache-Control: private, max-age=0, no-cache, no-store
    // Request duration: 0.603163s
