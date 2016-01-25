.. _ex/simple-events:

/v1/services/simple/events
==========================

**Request**:

.. sourcecode:: http

    GET http://ticketscloud.org/v1/services/simple/events
    Authorization: key 047bdb8bcee44d3693371920aaf9135c
    Accept: application/json
    Content-Type: application/json

**Response**:

.. sourcecode:: http

    [
      {
        "id": "568a22b5f06c5a42975fb913",
        "deal": null,
        "venue": {
          "id": "554111c09cb538793e6a3c37",
          "country": {
            "id": "RU",
            "name": {
              "fr": "Russie",
              "en": "Russia",
              "zh": "俄罗斯",
              "be": "Расійская Федэрацыя",
              "ru": "Россия",
              "default": "Russia"
            }
          },
          "name": "16 тонн",
          "address": "Пресненский вал, дом 6, строение 1",
          "point": {
            "coordinates": [
              37.56434200000001,
              55.76430800000001
            ],
            "type": "Point"
          },
          "city": {
            "id": 524901,
            "country": "RU",
            "name": {
              "fr": "Moscou",
              "en": "Moscow",
              "zh": "莫斯科",
              "be": "Горад Масква",
              "ru": "Москва",
              "default": "Moscow"
            },
            "timezone": "Europe/Moscow"
          },
          "desc": null
        },
        "status": "stand_by",
        "sets": [
          {
            "id": "568a22b6f06c5a42985fb914",
            "name": "fdfd",
            "price_extra": "0.00",
            "rules": [
              {
                "id": "56a61828f06c5a059b937fdc",
                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160102T210000Z\r\nDTEND;VALUE=DATE-TIME:20160128T205900Z\r\nEND:VEVENT\r\n",
                "price_org": "100.00",
                "current": true,
                "price": "100.00",
                "price_extra": "0.00"
              }
            ],
            "amount_vacant": 3,
            "price_org": "100.00",
            "pos": 0,
            "price": "100.00",
            "sector": null,
            "amount": 3,
            "seats": null
          }
        ],
        "updated_at": "2016-01-25T12:42:22.645000+00:00",
        "partner": {
          "id": "56810047f06c5a6ac62f4e1d",
          "tags": [],
          "desc": "description",
          "media": null,
          "contact": {
            "www": "v_test_6UYDD.com",
            "name": "",
            "address": "Россия г. Москва, ул. Жуковского д. 17 к. 2, 6UYDD",
            "phones": [
              "8-916-768-32-32"
            ],
            "email": "vsuharnikov+6uydd@gmail.com"
          },
          "name": "v_test_6UYDD brand"
        },
        "created_at": "2016-01-04T07:43:49.793000+00:00",
        "org": {
          "id": "56810047f06c5a6ac62f4e1d",
          "tags": [],
          "desc": "description",
          "media": null,
          "contact": {
            "www": "v_test_6UYDD.com",
            "name": "",
            "address": "Россия г. Москва, ул. Жуковского д. 17 к. 2, 6UYDD",
            "phones": [
              "8-916-768-32-32"
            ],
            "email": "vsuharnikov+6uydd@gmail.com"
          },
          "name": "v_test_6UYDD brand"
        },
        "ticket_template": {
          "fan_cover_url": null,
          "name": null,
          "text_color": null
        },
        "tags": [
          "выставки"
        ],
        "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160127T210000Z\r\nDTEND;VALUE=DATE-TIME:20160128T205900Z\r\nEND:VEVENT\r\n",
        "title": {
          "text": "test",
          "desc": "test"
        },
        "map": null,
        "media": null,
        "age_rating": 0,
        "tickets_amount": 3,
        "tickets_amount_vacant": 3
      }
    ]
    // GET http://dev.ticketscloud.org/v1/services/simple/events
    // HTTP/1.1 200 OK
    // Server: nginx/1.8.0
    // Date: Mon, 25 Jan 2016 13:10:11 GMT
    // Content-Type: application/json; charset=UTF-8
    // Content-Length: 2848
    // Connection: keep-alive
    // X-Partner: 56810047f06c5a6ac62f4e1d
    // Cache-Control: private, max-age=0, no-cache, no-store
    // Request duration: 0.116911s
