.. _simpleevents:
.. _api/services/simple/events:

Simple service for lazy integration
===================================

.. http:get:: /v1/services/simple/events

    Returns comprehensive information about available events.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :query updated_at__gt: Returns events which were updated since the specified
        date. The date should be defined in `ISO-8601
        <https://en.wikipedia.org/wiki/ISO_8601>`_ format.
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr datetime created_at: :ref:`Event <event>` creation timestamp
    :>jsonarr object deal: :ref:`Deal <deal>` terms
    :>jsonarr string id: :ref:`Event <event>` id
    :>jsonarr string lifetime: :ref:`Event <event>` duration in :rfc:`iCal format <5545>`
    :>jsonarr object org: :ref:`Organizer <partner>` information object
    :>jsonarr array media: :ref:`Media files <att>`
    :>jsonarr array sets: List of available :ref:`sets <set>` including:

        - **amount** (*number*): Amount of available :ref:`tickets <ticket>` in set
        - **id** (*string*): :ref:`Set <set>` id
        - **name** (*string*): Description
        - **price** (*string*): Cost of single ticket including the terms from the current rule
        - **price_extra** (*string*): Extra price on top of base one
        - **price_org** (*string*): Base price for tickets provided by a organizer
        - **rules** (*array* of *objects*): List of rules applicable to this set. The current one is defined by the flag ``current: true``

    :>jsonarr array tags: List of :ref:`event <event>` tags
    :>jsonarr object title: :ref:`Event <event>` name and description
    :>jsonarr datetime updated_at: :ref:`Event <event>` last update timestamp
    :>jsonarr object venue: :ref:`Venue <venue>` information object
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

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
                "media": {
                    "logo": {
                        "author": "535fb19bdca6a9d1638f2007",
                        "content_type": "image/jpeg",
                        "id": "545b686b37abbd08a96e50a5",
                        "length": 72122,
                        "md5hash": "0db79df4bbef2e847e31e46508f1d43e",
                        "url": "https://s3-eu-west-1.amazonaws.com/media.ticketscloud/9a44bb963ae44db8a443d1f3c19ed39e.jpeg"
                    }
                },
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
                        "amount_vacant": 13,
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
                        "amount_vacant": 13,
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

    Returns comprehensive information about specific event.

    :param idevent: :ref:`Event <event>` id
    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :query updated_at__gt: Returns events which were updated since the specified
        date. The date should be defined in `ISO-8601
        <https://en.wikipedia.org/wiki/ISO_8601>`_ format.
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: :ref:`Event <event>` creation timestamp
    :>json object deal: :ref:`Deal <deal>` terms
    :>json string id: :ref:`Event <event>` id
    :>json string lifetime: :ref:`Event <event>` duration in :rfc:`iCal format <5545>`
    :>json object org: :ref:`Organizer <partner>` information object
    :>json array media: :ref:`Media files <att>`
    :>json array sets: List of available :ref:`sets <set>` including:

        - **amount** (*number*): Amount of available :ref:`tickets <ticket>` in set
        - **id** (*string*): :ref:`Set <set>` id
        - **name** (*string*): Description
        - **price** (*string*): Cost of single ticket including the terms from the current rule
        - **price_extra** (*string*): Extra price on top of base one
        - **price_org** (*string*): Base price for tickets provided by a organizer
        - **rules** (*array* of *objects*): List of rules applicable to this set. The current one is defined by the flag ``current: true``

    :>json array tags: List of :ref:`event <event>` tags
    :>json object title: :ref:`Event <event>` name and description
    :>json datetime updated_at: :ref:`Event <event>` last update timestamp
    :>json object venue: :ref:`Venue <venue>` information object
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

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
            "media": {
                "logo": {
                    "author": "535fb19bdca6a9d1638f2007",
                    "content_type": "image/jpeg",
                    "id": "545b686b37abbd08a96e50a5",
                    "length": 72122,
                    "md5hash": "0db79df4bbef2e847e31e46508f1d43e",
                    "url": "https://s3-eu-west-1.amazonaws.com/media.ticketscloud/9a44bb963ae44db8a443d1f3c19ed39e.jpeg"
                }
            },
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
                    "amount_vacant": 13,
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
