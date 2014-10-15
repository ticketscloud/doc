.. _api/geo:

========
Geo Data
========


.. _api/resources/countries:

Countries
=========

.. http:get:: /v1/resources/countries
    :synopsis: Returns list of countries

    Returns list of countries.

    :<header Accept: :mimetype:`application/json`
    :>header Content-Type: :mimetype:`application/json`
    :query string ids: List of object ids to return
    :query number limit: Limit returned collection by specified number
    :query number offset: Skip specified number of object from start
    :query string suggest: Asks to suggest the countries which contains
                           specified substring
    :query string fields-schema: :ref:`api/dsl`
    :>jsonarr string id: Country ID
    :>jsonarr object name: Mapping of locale to localized name
    :>jsonarr string type: Object type
    :code 200: OK

    **Request**:

    .. sourcecode:: http

        GET /v1/resources/countries?limit=4 HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org

    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "id": "AF",
                "name": {
                    "default": "Afghanistan",
                    "en": "Afghanistan"
                },
                "type": "country"
            },
            {
                "id": "AX",
                "name": {
                    "default": "Aland Islands",
                    "en": "Aland Islands"
                },
                "type": "country"
            },
            {
                "id": "AL",
                "name": {
                    "default": "Albania",
                    "en": "Albania"
                },
                "type": "country"
            },
            {
                "id": "DZ",
                "name": {
                    "default": "Algeria",
                    "en": "Algeria"
                },
                "type": "country"
            }
        ]


    When you don't really know which country you're looking for, you can pass
    `suggest` query parameter to filter alike countries by the specified name:

    **Request**:

    .. sourcecode:: http

        GET /v1/resources/countries?suggest=Rus HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org

    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "id": "RU",
                "name": {
                    "default": "Russia",
                    "en": "Russia"
                },
                "type": "country"
            }
        ]


.. _api/resources/cities:

Cities
======

.. http:get:: /v1/resources/cities
    :synopsis: Returns list of cities

    Returns list of cities.

    :<header Accept: :mimetype:`application/json`
    :>header Content-Type: :mimetype:`application/json`
    :query string ids: List of object ids to return
    :query number limit: Limit returned collection by specified number
    :query number offset: Skip specified number of object from start
    :query string suggest: Asks to suggest the countries which contains
                           specified substring
    :query str sort: sort by field in django-style
                     ("population" or "-populanion")
    :query string fields-schema: :ref:`api/dsl`
    :>jsonarr string country: Country ID
    :>jsonarr object id: City ID
    :>jsonarr object name: Mapping of locale to localized name
    :>jsonarr string timezone: Timezone in Olson database format
    :>jsonarr string type: Object type
    :>jsonarr int populanion: populanion
    :code 200: OK

    **Request**:

    .. code-block:: http

        GET /v1/resources/cities?country=ru&sort=-population&limit=2 HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Type: application/json; charset=UTF-8
        Server: nginx
        Transfer-Encoding: chunked

        [
            {
                "name": {
                    "be": "\u0413\u043e\u0440\u0430\u0434 \u041c\u0430\u0441\u043a\u0432\u0430",
                    "fr": "Moscou",
                    "ru": "\u041c\u043e\u0441\u043a\u0432\u0430",
                    "default": "Moscow",
                    "en": "Moscow",
                    "zh": "\u83ab\u65af\u79d1"
                },
                "country": "RU",
                "type": "city",
                "population": 10381222,
                "id": 524901,
                "timezone": "Europe/Moscow"
            },
            {
                "name": {
                    "default": "Saint Petersburg",
                    "en": "Saint-Petersburg",
                    "fr": "Saint-P\u00e9tersbourg",
                    "ru": "\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433"
                },
                "country": "RU",
                "type": "city",
                "population": 5028000,
                "id": 498817,
                "timezone": "Europe/Moscow"
            }
        ]
