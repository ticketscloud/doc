=====
Deals
=====

Deals are required to start `ticket` sales on specific :ref:`event` since
they are defines the final price for them depending on various `conditions`.


.. _deal:
.. _api/resources/deal:

Deal
====

.. http:get:: /v0/resources/deals/{iddeal}
    :synopsis: Return information about a deal

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string partner: filter for obj or subj
    :query string status: filter for status
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: Deal creation timestamp
    :>json string event: :ref:`event` ID
    :>json string id: :ref:`deal` ID
    :>json string obj: :ref:`partner` ID
    :>json boolean reversed_deal: Deal made from `subj` to `obj`
    :>json string status: Deal status
    :>json string subj: :ref:`partner` ID
    :>json object term: Deal :ref:`terms`
    :>json object title: Title and description
    :>json datetime updated_at: Deal update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

.. http:patch:: /v0/resources/deals/{iddeal}
    :synopsis: Updates a deal

    Updates a :ref:`deal`.

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json boolean reversed_deal: Make deal reversed
    :<json string status: New deal status
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: Deal creation timestamp
    :>json string event: :ref:`event` ID
    :>json string id: :ref:`deal` ID
    :>json string obj: :ref:`partner` ID
    :>json boolean reversed_deal: Deal made from `subj` to `obj`
    :>json string status: Deal status
    :>json string subj: :ref:`partner` ID
    :>json object term: Deal :ref:`terms`
    :>json object title: Title and description
    :>json datetime updated_at: Deal update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. _api/resources/deals:

Deals
=====

.. http:get:: /v0/resources/deals
    :synopsis: Returns list of active deals

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr datetime created_at: Deal creation timestamp
    :>jsonarr string event: :ref:`event` ID
    :>jsonarr string id: :ref:`deal` ID
    :>jsonarr string obj: :ref:`partner` ID
    :>jsonarr boolean reversed_deal: Deal made from `subj` to `obj`
    :>jsonarr string status: Deal status
    :>jsonarr string subj: :ref:`partner` ID
    :>jsonarr object term: Deal :ref:`terms`
    :>jsonarr object title: Title and description
    :>jsonarr datetime updated_at: Deal update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    .. code-block:: http

        GET /v0/resources/deals HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Host: ticketscloud.org


    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "created_at": null,
                "event": "5357baaff51600525c9e1397",
                "id": "535fb1f1dca6a9d1638f2008",
                "obj": "5357b929f51600525c9e1396",
                "reversed_deal": null,
                "status": "accepted",
                "subj": "535fb19bdca6a9d1638f2007",
                "term": {
                    "core": "3.00%",
                    "extra": "10.0%",
                    "org": "91.00%",
                    "pfc": false
                },
                "updated_at": null
            }
        ]


.. http:post:: /v0/resources/deals
    :synopsis: Creates a new deal

    Creates a new :ref:`deal`.

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string event: :ref:`event` ID
    :<json string subj: :ref:`partner` ID
    :<json object term: Deal :ref:`terms`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr datetime created_at: Deal creation timestamp
    :>json string event: :ref:`event` ID
    :>json string id: :ref:`deal` ID
    :>json string obj: :ref:`partner` ID
    :>json boolean reversed_deal: Deal made from `subj` to `obj`
    :>json string status: Deal status
    :>json string subj: :ref:`partner` ID
    :>json object term: Deal :ref:`terms`
    :>json object title: Title and description
    :>json datetime updated_at: Deal update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    .. code-block:: http

        POST /v0/resources/deals HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Content-Length: 118
        Content-Type: application/json; charset=utf-8
        Host: ticketscloud.org

        {
            "event": "5368b3d49583cb96a0357590",
            "subj": "5357b929f51600525c9e1396",
            "term": {
                "extra": 10,
                "org": 10,
                "pfc": true
            }
        }

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "created_at": "2014-08-18 16:42:29.534470+00:00",
            "event": "5368b3d49583cb96a0357590",
            "id": "545fb1f1dca6a9d1638f3192",
            "obj": "53f1f4a9e0ce77186cf52d1f",
            "reversed_deal": null,
            "status": "accepted",
            "subj": "5357b929f51600525c9e1396",
            "term": {
                "core": "10.00%",
                "extra": "10.0%",
                "org": "10.00%",
                "pfc": true
            },
            "updated_at": "2014-08-18 16:42:29.534470+00:00"
        }


.. _terms:

Deal Terms
==========

Deal terms is an immutable object which stored within the :ref:`deal` object
with the following fields:

    * **org** (string): Amount of price which :ref:`organizer <partner>` will
      get
    * **extra** (string): Extra price set by :ref:`agent <partner>`
    * **core** (string): TicketsCloud commission
    * **pfc** (boolean): Payment-For-Customer. When ``true`` customer pays
        the bill.

Each `org`, `extra` and `core` value may have absolute value and relative
(percentage) ration from the base ticket price.
