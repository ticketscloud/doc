.. _simpleevents:
.. _api/services/simple/events:

Simple service for lazy integration
===================================

.. http:get:: /v1/services/simple/events

    :query updated_at__gt: Returns events which were updated since the specified
        date. The date should be defined in `ISO-8601
        <https://en.wikipedia.org/wiki/ISO_8601>`_ format.

    **Request**

    .. code-block:: http

        GET /v1/services/simple/events HTTP/1.1
        Accept: application/json
        Authorization: key your-very-secret-key
        Host: ticketscloud.org

    **Response**

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "created_at": "2014-09-19T10:30:24.388000+00:00",
                "deal": {
                    "extra": "10.0%",
                    "pfc": false
                },
                "id": "541c05c037abbd1af8b3398e",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART:20141001T170000Z\r\nDTEND:20141001T190000Z\r\nEND:VEVENT\r\n",
                "org": {
                    "contact": {},
                    "desc": null,
                    "id": "5357b929f51600525c9e1396",
                    "name": "Organizator",
                    "tags": []
                },
                "sets": [
                    {
                        "amount": 100,
                        "id": "541c05c037abbd1af8b33992",
                        "name": "foo",
                        "price": "1105.5",
                        "price_extra": "100.5",
                        "price_org": "1005.00",
                        "rules": [
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART:20140901T170000Z\r\nDTEND:20141001T190000Z\r\nEND:VEVENT\r\n",
                                "current": true,
                                "id": "541c05c037abbd1af8b33990",
                                "price": "1105.5",
                                "price_extra": "100.5",
                                "price_org": "1005.00"
                            }
                        ]
                    }
                ],
                "tags": [
                    "концерты",
                    "вечеринки"
                ],
                "title": {
                    "desc": "Возвращение музыканта в хорошем расположении духа и с новой программой",
                    "text": "Найк Борзов"
                },
                "updated_at": "2014-09-19T10:30:24.793000+00:00",
                "venue": {
                    "address": "Кутузовский просп., 25",
                    "city": {},
                    "country": {},
                    "desc": "Представления с участием кошек и Куклачевых",
                    "id": "53eca6fd0fc5f66be2610d8c",
                    "name": "Театр кошек Юрия Куклачева",
                    "point": {
                        "coordinates": [
                            55.7444151,
                            37.5458909
                        ],
                        "type": "Point"
                    }
                }
            },
            {
                "created_at": "2014-09-19T11:10:31.922000+00:00",
                "deal": {
                    "extra": "10.0%",
                    "pfc": false
                },
                "id": "541c0f2737abbd1c64b61b48",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART:20141001T170000Z\r\nDTEND:20141001T190000Z\r\nEND:VEVENT\r\n",
                "org": {
                    "contact": {},
                    "desc": null,
                    "id": "5357b929f51600525c9e1396",
                    "name": "Organizator",
                    "tags": []
                },
                "sets": [
                    {
                        "amount": 100,
                        "id": "541c0f2737abbd1c64b61b4c",
                        "name": "foo",
                        "price": "1105.5",
                        "price_extra": "100.5",
                        "price_org": "1005.00",
                        "rules": [
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART:20140901T170000Z\r\nDTEND:20141001T190000Z\r\nEND:VEVENT\r\n",
                                "current": true,
                                "id": "541c0f2737abbd1c64b61b4a",
                                "price": "1105.5",
                                "price_extra": "100.5",
                                "price_org": "1005.00"
                            }
                        ]
                    }
                ],
                "tags": [
                    "концерты",
                    "вечеринки"
                ],
                "title": {
                    "desc": "Возвращение музыканта в хорошем расположении духа и с новой программой",
                    "text": "Найк Борзов"
                },
                "updated_at": "2014-09-19T11:10:32.235000+00:00",
                "venue": {
                    "address": "Кутузовский просп., 25",
                    "city": {},
                    "country": {},
                    "desc": "Представления с участием кошек и Куклачевых",
                    "id": "53eca6fd0fc5f66be2610d8c",
                    "name": "Театр кошек Юрия Куклачева",
                    "point": {
                        "coordinates": [
                            55.7444151,
                            37.5458909
                        ],
                        "type": "Point"
                    }
                }
            }
        ]



.. http:get:: /v1/services/simple/events/{idevent}

Return specific event with additional information.

    **Request**

    .. code-block:: http

        GET /v1/services/simple/events/5357baaff51600525c9e1397 HTTP/1.1
        Accept: application/json
        Authorization: key your-very-secret-key
        Host: ticketscloud.org

    **Response**

    .. code-block:: http


        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "created_at": "2014-09-19T10:30:24.388000+00:00",
            "deal": {
                "extra": "10.0%",
                "pfc": false
            },
            "id": "541c05c037abbd1af8b3398e",
            "lifetime": "BEGIN:VEVENT\r\nDTSTART:20141001T170000Z\r\nDTEND:20141001T190000Z\r\nEND:VEVENT\r\n",
            "org": {
                "contact": {},
                "desc": null,
                "id": "5357b929f51600525c9e1396",
                "name": "Organizator",
                "tags": []
            },
            "sets": [
                {
                    "amount": 100,
                    "id": "541c05c037abbd1af8b33992",
                    "name": "foo",
                    "price": "1105.5",
                    "price_extra": "100.5",
                    "price_org": "1005.00",
                    "rules": [
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART:20140901T170000Z\r\nDTEND:20141001T190000Z\r\nEND:VEVENT\r\n",
                            "current": true,
                            "id": "541c05c037abbd1af8b33990",
                            "price": "1105.5",
                            "price_extra": "100.5",
                            "price_org": "1005.00"
                        }
                    ]
                }
            ],
            "tags": [
                "концерты",
                "вечеринки"
            ],
            "title": {
                "desc": "Возвращение музыканта в хорошем расположении духа и с новой программой",
                "text": "Найк Борзов"
            },
            "updated_at": "2014-09-19T10:30:24.793000+00:00",
            "venue": {
                "address": "Кутузовский просп., 25",
                "city": {},
                "country": {},
                "desc": "Представления с участием кошек и Куклачевых",
                "id": "53eca6fd0fc5f66be2610d8c",
                "name": "Театр кошек Юрия Куклачева",
                "point": {
                    "coordinates": [
                        55.7444151,
                        37.5458909
                    ],
                    "type": "Point"
                }
            }
        }
