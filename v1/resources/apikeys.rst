========
API Keys
========

.. _apikey:
.. _api/resources/partners/api_key:

API Key
=======

API Key is an unique token which uses for :ref:`partner` authentication.
This key should be specified as value for :header:`Authorization` on each
request that been made to TicketsCloud API.

.. http:get:: /v1/resources/partners/{idpartner}/api_keys/{idkey}
    :synopsis: Returns an API key information

    Returns an information about API key.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idpartner: :ref:`partner` ID
    :param string idkey: :ref:`apikey` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: API key creation timestamp
    :>json string id: :ref:`apikey` ID
    :>json string key: API key itself
    :>json string name: API key name
    :>json string partner: Related :ref:`partner` ID
    :>json boolean removed: Removed flag
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/partners/535fb19bdca6a9d1638f2007/api_keys/53f1d89437abbd0a9ca87882 HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "created_at": "2014-08-18T10:42:28.288000+00:00",
            "id": "53f1d89437abbd0a9ca87882",
            "key": "48de25a3c7f84996bc3c183c640f9948",
            "name": "new-key",
            "partner": "535fb19bdca6a9d1638f2007",
            "removed": false
        }



.. http:patch:: /v1/resources/partners/{idpartner}/api_keys/{idkey}
    :synopsis: Updates API key information

    Updates API key information.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idpartner: :ref:`partner` ID
    :param string idkey: :ref:`apikey` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string name: API key name
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: API key creation timestamp
    :>json string id: :ref:`apikey` ID
    :>json string key: API key itself
    :>json string name: API key name
    :>json string partner: Related :ref:`partner` ID
    :>json boolean removed: Removed flag
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


    **Request**:

    .. code-block:: http

        PATCH /v1/resources/partners/535fb19bdca6a9d1638f2007/api_keys/53f1d89437abbd0a9ca87882 HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Content-Length: 21
        Content-Type: application/json; charset=utf-8
        Host: ticketscloud.org

        {
            "name": "new-name"
        }


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "created_at": "2014-08-18T10:42:28.288000+00:00",
            "id": "53f1d89437abbd0a9ca87882",
            "key": "48de25a3c7f84996bc3c183c640f9948",
            "name": "new-name",
            "partner": "535fb19bdca6a9d1638f2007",
            "removed": false
        }


.. http:delete:: /v1/resources/partners/{idparner}/api_keys/{idkey}
    :synopsis: Removes an API key

    Removes an API key.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idpartner: :ref:`partner` ID
    :param string idkey: :ref:`apikey` ID
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        DELETE /v1/resources/partners/535fb19bdca6a9d1638f2007/api_keys/53f1d89437abbd0a9ca87882 HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {}


.. _api/resources/partners/api_keys:

API Keys
========

Manages :ref:`apikey` collection of specific :ref:`partner`.

.. http:get:: /v1/resources/partners/{idpartner}/api_keys
    :synopsis: Returns list of API keys

    Returns list of API keys which :ref:`partner` has.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idpartner: :ref:`partner` ID
    :query string ids: List of IDs to return
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr datetime created_at: API key creation timestamp
    :>jsonarr string id: :ref:`apikey` ID
    :>jsonarr string key: API key itself
    :>jsonarr string name: API key name
    :>jsonarr string partner: Related :ref:`partner` ID
    :>jsonarr boolean removed: Removed flag
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/partners/535fb19bdca6a9d1638f2007/api_keys HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "created_at": "2014-08-18T10:30:02.516000+00:00",
                "id": "53f1d5aa37abbd0a9da87882",
                "key": "my-very-secret-key",
                "name": "test",
                "partner": "535fb19bdca6a9d1638f2007",
                "removed": false
            },
            {
                "created_at": "2014-08-18T10:30:23.487000+00:00",
                "id": "53f1d5bf37abbd0a9ea87882",
                "key": "5a1428de2cd84b5189453470dffa3b5d",
                "name": "default",
                "partner": "535fb19bdca6a9d1638f2007",
                "removed": false
            },
            {
                "created_at": "2014-08-18T10:31:01.930000+00:00",
                "id": "53f1d5e537abbd0a9da87883",
                "key": "aaef4478264a4be2b2c9838efa8df7c6",
                "name": "crm",
                "partner": "535fb19bdca6a9d1638f2007",
                "removed": false
            }
        ]


.. http:post:: /v1/resources/partners/{idpartner}/api_keys
    :synopsis: Creates a new API key

    Creates a new :ref:`apikey`.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idpartner: :ref:`partner` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string name: API key name
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: API key creation timestamp
    :>json string id: :ref:`apikey` ID
    :>json string key: API key itself
    :>json string name: API key name
    :>json string partner: Related :ref:`partner` ID
    :>json boolean removed: Removed flag
    :code 201: Created
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


    **Request**:

    .. code-block:: http

        POST /v1/resources/partners/535fb19bdca6a9d1638f2007/api_keys HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Content-Length: 20
        Content-Type: application/json; charset=utf-8
        Host: ticketscloud.org

        {
            "name": "new-key"
        }


    **Response**:

    .. code-block:: http

        HTTP/1.1 201 Created
        Content-Length: 203
        Content-Type: application/json; charset=UTF-8

        {
            "created_at": "2014-08-18T10:42:28.288420+00:00",
            "id": "53f1d89437abbd0a9ca87882",
            "key": "48de25a3c7f84996bc3c183c640f9948",
            "name": "new-key",
            "partner": "535fb19bdca6a9d1638f2007",
            "removed": false
        }
