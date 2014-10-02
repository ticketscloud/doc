========
Partners
========

.. _partner:
.. _api/resources/partner:

Partner
=======

Partner is an special kind of :ref:`user` which manages event, provides tickets
and sign contracts with others. It's different since in most cases single
Partner represents some organization which may be managed by multiple different
:ref:`users <user>`. People come and gone, partners are more persistent thing
in the world.


.. http:get:: /v1/resources/partners/{idpartner}
    :synopsis: Returns partner information

    Returns partner information.

    :<header Accept: :mimetype:`application/json`
    :param string idpartner: :ref:`partner` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string channels: Partner creation timestamp
    :>json object contact: Contact information
    :>json datetime created_at: Partner creation timestamp
    :>json string desc: Description
    :>json string director: CEO
    :>json string id: Partner ID
    :>json object legal: Related Legal
    :>json string name: Partner name
    :>json array media: :ref:`Media files <att>`
    :>json boolean removed: Deleted flag
    :>json array roles: Assigned roles
    :>json array tags: Tags
    :>json datetime updated_at: Partner update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/partners/535fb19bdca6a9d1638f2007 HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "channels": "Все доступные каналы распространения",
            "contact": {
                "address": "г.Москва, ул. Берсеневский переулок, 2с1",
                "email": "info@nanobilet.ru",
                "id": null,
                "phones": ["+79101002030"],
                "www": "http://nanobilet.ru"
            },
            "created_at": null,
            "desc": "Первый агент системы",
            "director": "Егор Егерев",
            "id": "535fb19bdca6a9d1638f2007",
            "legal": null,
            "name": "Nanobilet",
            "removed": false,
            "roles": ["agent"],
            "tags": ["музыка", "вечеринки", "концерты"],
            "updated_at": null,
            "user": {
                "created_at": null,
                "email": "ag@tc.ru",
                "first_name": "Егор",
                "id": "535fb11ddca6a9d1638f2006",
                "last_name": "Егерев",
                "partners": ["535fb19bdca6a9d1638f2007"],
                "tags": [],
                "updated_at": null
            }
        }

.. http:patch:: /v1/resources/partners/{idpartner}
    :synopsis: Updates specific partner fields

    Updates specific partner fields.

    :<header Accept: :mimetype:`application/json`
    :param string idpartner: :ref:`partner` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string channels: Partner creation timestamp
    :<json object contact: Contact information
    :<json string desc: Description
    :<json string director: CEO
    :<json object legal: Related Legal
    :<json string name: Partner name
    :<json array media: :ref:`Media files <att>`
    :<json boolean removed: Deleted flag
    :<json array roles: Assigned roles
    :<json array tags: Tags
    :<json datetime updated_at: Partner update timestamp
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string channels: Partner creation timestamp
    :>json object contact: Contact information
    :>json datetime created_at: Partner creation timestamp
    :>json string desc: Description
    :>json string director: CEO
    :>json string id: Partner ID
    :>json object legal: Related Legal
    :>json array media: :ref:`Media files <att>`
    :>json string name: Partner name
    :>json boolean removed: Deleted flag
    :>json array roles: Assigned roles
    :>json array tags: Tags
    :>json datetime updated_at: Partner update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. _api/resources/partners:

Partners
========

Collection of :ref:`partner` objects.

.. http:get:: /v1/resources/partners
    :synopsis: Returns list of Partners

    Returns list of :ref:`partner` objects.

    :<header Accept: :mimetype:`application/json`
    :query string ids: List of IDs to return
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string channels: Partner creation timestamp
    :>json object contact: Contact information
    :>json datetime created_at: Partner creation timestamp
    :>json string desc: Description
    :>json string director: CEO
    :>json string id: Partner ID
    :>json object legal: Related Legal
    :>json array media: :ref:`Media files <att>`
    :>json string name: Partner name
    :>json boolean removed: Deleted flag
    :>json array roles: Assigned roles
    :>json array tags: Tags
    :>json datetime updated_at: Partner update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/partners HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "channels": null,
                "contact": {},
                "created_at": null,
                "desc": null,
                "director": null,
                "id": "5357b929f51600525c9e1396",
                "legal": null,
                "name": "Organizator",
                "removed": false,
                "roles": ["org"],
                "tags": [],
                "updated_at": null,
                "user": {
                    "created_at": null,
                    "email": "org@tc.ru",
                    "first_name": "Org",
                    "id": "53555b2256c02c17cb75791c",
                    "last_name": "Organizator",
                    "partners": ["5357b929f51600525c9e1396"],
                    "tags": [],
                    "updated_at": null
                }
            },
            {
                "channels": "Все доступные каналы распространения",
                "contact": {
                    "address": "г.Москва, ул. Берсеневский переулок, 2с1",
                    "email": "info@nanobilet.ru",
                    "id": null,
                    "phones": ["+79101002030"],
                    "www": "http://nanobilet.ru"
                },
                "created_at": null,
                "desc": "Первый агент системы",
                "director": "Егор Егерев",
                "id": "535fb19bdca6a9d1638f2007",
                "legal": null,
                "name": "Nanobilet",
                "removed": false,
                "roles": ["agent"],
                "tags": ["музыка", "вечеринки", "концерты"],
                "updated_at": null,
                "user": {
                    "created_at": null,
                    "email": "ag@tc.ru",
                    "first_name": "Егор",
                    "id": "535fb11ddca6a9d1638f2006",
                    "last_name": "Егерев",
                    "partners": ["535fb19bdca6a9d1638f2007"],
                    "tags": [],
                    "updated_at": null
                }
            }
        ]
