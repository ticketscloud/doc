======
Events
======

.. _event:
.. _api/resources/event:

Event
=====

.. http:get:: /v0/resources/events/{idevent}
    :synopsis: Returns information about the event

    Returns information about the event.

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: Event creation timestamp
    :>json string id: :ref:`event` ID
    :>json string lifetime: Event lifetime in iCal format
    :>json string org: :ref:`Organizer <partner>` ID
    :>json object place: Information about event location
    :>json boolean removed: Deletion flag
    :>json string status: Event status
    :>json array tags: Event tags
    :>json object title: Title and description
    :>json datetime updated_at: Event update timestamp
    :>json venue: Event venue
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v0/resources/events/5357baaff51600525c9e1397 HTTP/1.1
        Accept: application/json
        Authorization: key my-secret-api-key
        Host: ticketscloud.ru


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "created_at": null,
            "id": "5357baaff51600525c9e1397",
            "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140710T000000\r\nDTEND;VALUE=DATE-TIME:20140910T000000\r\nEND:VEVENT\r\n",
            "org": "5357b929f51600525c9e1396",
            "place": {
                "address": "Театр кошек Юрия Куклачева",
                "city": null,
                "country": null,
                "point": null
            },
            "removed": false,
            "status": "public",
            "tags": [
                "кошка",
                "мука"
            ],
            "title": {
                "desc": null,
                "text": "Семинар: милые котята"
            },
            "updated_at": null,
            "venue": null
        }


.. _api/resources/events:

Events
======

.. http:get:: /v0/resources/events
    :synopsis: Returns list of existed events

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :query string filter: Custom filter
    :query string org: Filters events by :ref:`Organizer <partner>` ID
    :query boolean removed: Whenever include removed events
    :query string status: Filters events by their status
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr datetime created_at: Event creation timestamp
    :>jsonarr string id: :ref:`event` ID
    :>jsonarr string lifetime: Event lifetime in iCal format
    :>jsonarr string org: :ref:`Organizer <partner>` ID
    :>jsonarr object place: Information about event location
    :>jsonarr boolean removed: Deletion flag
    :>jsonarr string status: Event status
    :>jsonarr array tags: Event tags
    :>jsonarr object title: Title and description
    :>jsonarr datetime updated_at: Event update timestamp
    :>jsonarr venue: Event venue
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v0/resources/events?filter=my HTTP/1.1
        Accept: application/json
        Authorization: key my-secret-api-key
        Host: ticketscloud.ru

    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "created_at": null,
                "id": "5357baaff51600525c9e1397",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140710T000000\r\nDTEND;VALUE=DATE-TIME:20140910T000000\r\nEND:VEVENT\r\n",
                "org": "5357b929f51600525c9e1396",
                "place": {
                    "address": "Театр кошек Юрия Куклачева",
                    "city": null,
                    "country": null,
                    "point": null
                },
                "removed": false,
                "status": "public",
                "tags": [
                    "кошка",
                    "мука"
                ],
                "title": {
                    "desc": null,
                    "text": "Семинар: милые котята"
                },
                "updated_at": null,
                "venue": null
            },
            {
                "created_at": null,
                "id": "5368b3cc9583cb96a035758e",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140810T190000\r\nDTEND;VALUE=DATE-TIME:20140810T220000\r\nEND:VEVENT\r\n",
                "org": "5357b929f51600525c9e1396",
                "place": {
                    "address": "Arena Moscow",
                    "city": null,
                    "country": null,
                    "point": null
                },
                "removed": false,
                "status": "public",
                "tags": [
                    "концерты"
                ],
                "title": {
                    "desc": null,
                    "text": "MEGADETH"
                },
                "updated_at": null,
                "venue": null
            },
            {
                "created_at": null,
                "id": "5368b3d39583cb96a035758f",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140813T190000\r\nDTEND;VALUE=DATE-TIME:20140813T220000\r\nEND:VEVENT\r\n",
                "org": "5357b929f51600525c9e1396",
                "place": {
                    "address": "Стадион Лужники",
                    "city": null,
                    "country": null,
                    "point": null
                },
                "removed": false,
                "status": "public",
                "tags": [
                    "концерты"
                ],
                "title": {
                    "desc": null,
                    "text": "ДДТ. Презентация альбома «Прозрачный»"
                },
                "updated_at": null,
                "venue": null
            },
            {
                "created_at": null,
                "id": "5368b3d49583cb96a0357590",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20140916T210000\r\nDTEND;VALUE=DATE-TIME:20140916T230000\r\nEND:VEVENT\r\n",
                "org": "53555b2256c02c17cb75791c",
                "place": {
                    "address": "Клуб «Гараж»",
                    "city": null,
                    "country": null,
                    "point": null
                },
                "removed": false,
                "status": "public",
                "tags": [
                    "концерты"
                ],
                "title": {
                    "desc": null,
                    "text": "Смысловые Галлюцинации. 25 лет в темноте"
                },
                "updated_at": null,
                "venue": null
            }
        ]
