.. _ex/simple-events:

/v1/services/simple/events
==========================

**Request**:

.. sourcecode:: http

    GET /v1/services/simple/events HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Connection: keep-alive
    Host: dev.ticketscloud.org

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Cache-Control: private, max-age=0, no-cache, no-store
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json; charset=UTF-8
    Date: Mon, 25 Jan 2016 21:15:31 GMT
    Server: nginx/1.8.0
    Transfer-Encoding: chunked
    X-Partner: 56810047f06c5a6ac62f4e1d

    [
        {
            "id": "568a22b5f06c5a42975fb913",
            "age_rating": 0, 
            "created_at": "2016-01-04T07:43:49.793000+00:00", 
            "deal": null,  
            "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160127T210000Z\r\nDTEND;VALUE=DATE-TIME:20160128T205900Z\r\nEND:VEVENT\r\n", 
            "map": null, 
            "media": {}, 
            "org": {
                "id": "56810047f06c5a6ac62f4e1d",
                "contact": {
                    "address": "Россия г. Москва, ул. Жуковского д. 17 к. 2, 6UYDD", 
                    "email": "vsuharnikov+6uydd@gmail.com", 
                    "name": "", 
                    "phones": [
                        "8-916-768-32-32"
                    ], 
                    "www": "v_test_6UYDD.com"
                }, 
                "desc": "description", 
                "media": {}, 
                "name": "v_test_6UYDD brand", 
                "tags": []
            }, 
            "partner": {
                "id": "56810047f06c5a6ac62f4e1d",
                "contact": {
                    "address": "Россия г. Москва, ул. Жуковского д. 17 к. 2, 6UYDD", 
                    "email": "vsuharnikov+6uydd@gmail.com", 
                    "name": "", 
                    "phones": [
                        "8-916-768-32-32"
                    ], 
                    "www": "v_test_6UYDD.com"
                }, 
                "desc": "description", 
                "media": {}, 
                "name": "v_test_6UYDD brand", 
                "tags": []
            }, 
            "sets": [
                {
                    "id": "568a22b6f06c5a42985fb914",
                    "amount": 3, 
                    "amount_vacant": 1,  
                    "name": "fdfd", 
                    "pos": 0, 
                    "price": "100.00", 
                    "price_extra": "0.00", 
                    "price_org": "100.00", 
                    "rules": [
                        {
                            "id": "56a61828f06c5a059b937fdc",
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160102T210000Z\r\nDTEND;VALUE=DATE-TIME:20160128T205900Z\r\nEND:VEVENT\r\n", 
                            "current": true,  
                            "price": "100.00", 
                            "price_extra": "0.00", 
                            "price_org": "100.00"
                        }
                    ], 
                    "seats": null, 
                    "sector": null
                }
            ], 
            "status": "public", 
            "tags": [
                "выставки"
            ], 
            "ticket_template": {
                "fan_cover_url": null, 
                "name": null, 
                "text_color": null
            }, 
            "tickets_amount": 3, 
            "tickets_amount_vacant": 1, 
            "title": {
                "desc": "test", 
                "text": "test"
            }, 
            "updated_at": "2016-01-25T13:33:04.583000+00:00", 
            "venue": {
                "id": "554111c09cb538793e6a3c37",
                "address": "Пресненский вал, дом 6, строение 1", 
                "city": {
                    "id": 524901,
                    "country": "RU",  
                    "name": {
                        "be": "Горад Масква", 
                        "default": "Moscow", 
                        "en": "Moscow", 
                        "fr": "Moscou", 
                        "ru": "Москва", 
                        "zh": "莫斯科"
                    }, 
                    "timezone": "Europe/Moscow"
                }, 
                "country": {
                    "id": "RU", 
                    "name": {
                        "be": "Расійская Федэрацыя", 
                        "default": "Russia", 
                        "en": "Russia", 
                        "fr": "Russie", 
                        "ru": "Россия", 
                        "zh": "俄罗斯"
                    }
                }, 
                "desc": null, 
                "name": "16 тонн", 
                "point": {
                    "coordinates": [
                        37.56434200000001, 
                        55.76430800000001
                    ], 
                    "type": "Point"
                }
            }
        }, 
        {
            "id": "56a6253df06c5a059a93802e",
            "age_rating": 0, 
            "created_at": "2016-01-25T13:38:05.007000+00:00", 
            "deal": null,
            "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160512T200000Z\r\nDTEND;VALUE=DATE-TIME:20160513T195900Z\r\nEND:VEVENT\r\n", 
            "map": {
                "id": "54d79ee69cb538749c32c221",
                "desc": null,  
                "name": "default", 
                "sectors": [
                    {
                        "id": "54d7a0409cb538783b7bf8d5",
                        "desc": null,  
                        "name": "Партер"
                    }, 
                    {
                        "id": "54d7a0409cb538783b7bf8d6",
                        "desc": null, 
                        "name": "Балкон"
                    }
                ], 
                "svg": {
                    "map": {
                        "id": "54d7a0409cb538783b7bf8d7",
                        "author": null, 
                        "content_type": "image/svg+xml",  
                        "length": null, 
                        "md5hash": "9efaa9cf8af50f95a3ddf205f7bcebe0", 
                        "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/map/2015-02/54d79ee69cb538749c32c221-54d79ee69cb538749c32c220.svg"
                    }, 
                    "mapz": {
                        "id": "561c43a79cb5380fdcab402d",
                        "author": null, 
                        "content_type": "image/svg+xml", 
                        "length": null, 
                        "md5hash": "c77114baa0912d621044e8ad17f8aede", 
                        "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/map/2015-10/54d79ee69cb538749c32c221-54d79ee69cb538749c32c220.svgz"
                    }, 
                    "source": {
                        "id": "54d79ee69cb538749c32c220",
                        "author": null, 
                        "content_type": "image/svg+xml",  
                        "length": null, 
                        "md5hash": "d5bc921d747322b599f78987fa492c0b", 
                        "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/maps/2015-02/54d79ee69cb538749c32c220.svg"
                    }
                }
            }, 
            "media": {}, 
            "org": {
                "id": "56810047f06c5a6ac62f4e1d",
                "contact": {
                    "address": "Россия г. Москва, ул. Жуковского д. 17 к. 2, 6UYDD", 
                    "email": "vsuharnikov+6uydd@gmail.com", 
                    "name": "", 
                    "phones": [
                        "8-916-768-32-32"
                    ], 
                    "www": "v_test_6UYDD.com"
                }, 
                "desc": "description", 
                "media": {}, 
                "name": "v_test_6UYDD brand", 
                "tags": []
            }, 
            "partner": {
                "id": "56810047f06c5a6ac62f4e1d",
                "contact": {
                    "address": "Россия г. Москва, ул. Жуковского д. 17 к. 2, 6UYDD", 
                    "email": "vsuharnikov+6uydd@gmail.com", 
                    "name": "", 
                    "phones": [
                        "8-916-768-32-32"
                    ], 
                    "www": "v_test_6UYDD.com"
                }, 
                "desc": "description", 
                "media": {}, 
                "name": "v_test_6UYDD brand", 
                "tags": []
            }, 
            "sets": [
                {
                    "id": "56a6254bf06c5a059b93800c",
                    "amount": 3, 
                    "amount_vacant": 3,  
                    "name": "Партер", 
                    "pos": 0, 
                    "price": "100.00", 
                    "price_extra": "0.00", 
                    "price_org": "100.00", 
                    "rules": [
                        {
                            "id": "56a6254bf06c5a059b93800b",
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160123T200000Z\r\nDTEND;VALUE=DATE-TIME:20160513T195900Z\r\nEND:VEVENT\r\n", 
                            "current": true, 
                            "price": "100.00", 
                            "price_extra": "0.00", 
                            "price_org": "100.00"
                        }
                    ], 
                    "seats": {
                        "1": [
                            [
                                1, 
                                1
                            ], 
                            [
                                3, 
                                3
                            ], 
                            [
                                6, 
                                6
                            ]
                        ]
                    }, 
                    "sector": "54d7a0409cb538783b7bf8d5"
                }
            ], 
            "status": "public", 
            "tags": [
                "экскурсии"
            ], 
            "ticket_template": {
                "fan_cover_url": null, 
                "name": null, 
                "text_color": null
            }, 
            "tickets_amount": 3, 
            "tickets_amount_vacant": 3, 
            "title": {
                "desc": null, 
                "text": "With seats"
            }, 
            "updated_at": "2016-01-25T13:38:19.844000+00:00", 
            "venue": {
                "id": "54d49b9df06c5a0dbde10e7f",
                "address": "443010, г. Самара, ул. Фрунзе, д. 141", 
                "city": {
                    "id": 499099,
                    "country": "RU",
                    "name": {
                        "be": "Горад Самара", 
                        "default": "Samara", 
                        "en": "Samara", 
                        "fr": "Samara", 
                        "ru": "Самара", 
                        "zh": "薩馬拉"
                    }, 
                    "timezone": "Europe/Samara"
                }, 
                "country": {
                    "id": "RU", 
                    "name": {
                        "be": "Расійская Федэрацыя", 
                        "default": "Russia", 
                        "en": "Russia", 
                        "fr": "Russie", 
                        "ru": "Россия", 
                        "zh": "俄罗斯"
                    }
                }, 
                "desc": null, 
                "name": "Самарская Государственная Филармония", 
                "point": {
                    "coordinates": [
                        50.09498499999995, 
                        53.19151799999999
                    ], 
                    "type": "Point"
                }
            }
        }
    ]
