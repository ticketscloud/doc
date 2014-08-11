.. _simpleevents:
.. _api/services/simple/events:

Simple service for lazy integration
===================================

.. http:get:: /v0/services/simple/events

    **Request**

    .. code-block:: http

        GET /v0/services/simple/events HTTP/1.1
        Accept: application/json
        Authorization: key your-very-secret-key
        Host: ticketscloud.ru

    **Response**

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "deal": {
                    "extra": "10.0%",
                    "pfc": false
                },
                "event": {
                    "created_at": null,
                    "id": "5357baaff51600525c9e1397",
                    "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140710T000000\r\nDTEND;VALUE=DATE-TIME:20140910T000000\r\nEND:VEVENT\r\n",
                    "org": {
                        "contact": {},
                        "desc": null,
                        "id": "5357b929f51600525c9e1396",
                        "name": "Organizator",
                        "tags": []
                    },
                    "place": {
                        "address": "Театр кошек Юрия Куклачева",
                        "city": 524901,
                        "country": "RU",
                        "desc": null,
                        "name": null,
                        "point": {
                            "coordinates": [
                                55.75,
                                37.6167
                            ],
                            "type": "Point"
                        }
                    },
                    "tags": [
                        "кошка",
                        "мука"
                    ],
                    "title": {
                        "desc": null,
                        "text": "Семинар: милые котята"
                    },
                    "updated_at": null,
                    "venue": {}
                },
                "sets": [
                    {
                        "amount": 7,
                        "current_rule": {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140101T000000\r\nDTEND;VALUE=DATE-TIME:20171231T000000\r\nEND:VEVENT\r\n",
                            "id": "537368ff1b9bf9d05cca835a",
                            "price": "100.1"
                        },
                        "id": "5360a75a2b590f1c88e8680c",
                        "name": "Единственные",
                        "price": "100.1",
                        "rules": [
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140101T000000\r\nDTEND;VALUE=DATE-TIME:20171231T000000\r\nEND:VEVENT\r\n",
                                "id": "537368ff1b9bf9d05cca835a",
                                "price": "100.1"
                            },
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20180101T000000\r\nDTEND;VALUE=DATE-TIME:20201231T000000\r\nEND:VEVENT\r\n",
                                "id": "537369051b9bf9d05cca835b",
                                "price": "200.1"
                            }
                        ]
                    }
                ]
            }
        ]



.. http:get:: /v0/services/simple/events/{idevent}

Return specific event with additional information.

    **Request**

    .. code-block:: http

        GET /v0/services/simple/events/5357baaff51600525c9e1397 HTTP/1.1
        Accept: application/json
        Authorization: key your-very-secret-key
        Host: ticketscloud.ru

    **Response**

    .. code-block:: http


        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "deal": {
                "extra": "10.0%",
                "pfc": false
            },
            "event": {
                "created_at": null,
                "id": "5357baaff51600525c9e1397",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140710T000000\r\nDTEND;VALUE=DATE-TIME:20140910T000000\r\nEND:VEVENT\r\n",
                "org": {
                    "contact": {},
                    "desc": null,
                    "id": "5357b929f51600525c9e1396",
                    "name": "Organizator",
                    "tags": []
                },
                "place": {
                    "address": "Театр кошек Юрия Куклачева",
                    "city": 524901,
                    "country": "RU",
                    "desc": null,
                    "name": null,
                    "point": {
                        "coordinates": [
                            55.75,
                            37.6167
                        ],
                        "type": "Point"
                    }
                },
                "tags": [
                    "кошка",
                    "мука"
                ],
                "title": {
                    "desc": null,
                    "text": "Семинар: милые котята"
                },
                "updated_at": null,
                "venue": {}
            },
            "sets": [
                {
                    "amount": 7,
                    "current_rule": {
                        "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140101T000000\r\nDTEND;VALUE=DATE-TIME:20171231T000000\r\nEND:VEVENT\r\n",
                        "id": "537368ff1b9bf9d05cca835a",
                        "price": "100.1"
                    },
                    "id": "5360a75a2b590f1c88e8680c",
                    "name": "Единственные",
                    "price": "100.1",
                    "rules": [
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140101T000000\r\nDTEND;VALUE=DATE-TIME:20171231T000000\r\nEND:VEVENT\r\n",
                            "id": "537368ff1b9bf9d05cca835a",
                            "price": "100.1"
                        },
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20180101T000000\r\nDTEND;VALUE=DATE-TIME:20201231T000000\r\nEND:VEVENT\r\n",
                            "id": "537369051b9bf9d05cca835b",
                            "price": "200.1"
                        }
                    ]
                }
            ]
        }

