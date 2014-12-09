======
Orders
======

.. _order:
.. _api/resources/order:

Order
=====

.. http:get:: /v1/resources/orders/{idorder}
    :synopsis: Returns information about specified order

    Returns information about specified order.

    :<header Accept: :mimetype:`application/json`
    :param string idorder: :ref:`order` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json object customer: Customer information
    :>json datetime created_at: Partner creation timestamp
    :>json string deal: :ref:`deal` ID
    :>json string event: :ref:`event` ID
    :>json string id: :ref:`order` ID
    :>json datetime reserved_till: Related Legal
    :>json object rules: `Rules` mapping
    :>json string vendor: :ref:`vendor <partner>` ID
    :>json string status: Order status
    :>json array tickets: List of ordered `tickets` ids
    :>json array promocodes: List of `promocode` as objects
    :>json datetime updated_at: Partner update timestamp
    :>json value: Value
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "customer": {},
            "created_at": null,
            "deal": "535fb1f1dca6a9d1638f2008",
            "event": "5357baaff51600525c9e1397",
            "id": "537e1d95f05f951cded9cb02",
            "reserved_till": null,
            "rules": {
                "5360a75a2b590f1c88e8680c": "537368ff1b9bf9d05cca835a"
            },
            "vendor": null,
            "status": "executed",
            "tickets": [
                "537df47b6ab04735203a7219",
                "53b9421428422ec1b9cafbb5"
            ],
            "updated_at": null,
            "value": null
        }

.. http:patch:: /v1/resources/orders/{idorder}
    :synopsis: Updates order data

    Updates order data.

    :<header Accept: :mimetype:`application/json`
    :param string idorder: :ref:`order` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json object customer: Customer information
    :<json string status: Order status
    :<json array tickets: List of ordered `tickets` ids
    :<json bool all_or_nothing: reserve all tickets or not resetve nothing
    :<json array promocodes: List of `promocode` as strings (field `code`)
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json object customer: Customer information
    :>json datetime created_at: Partner creation timestamp
    :>json string deal: :ref:`deal` ID
    :>json string event: :ref:`event` ID
    :>json string id: :ref:`order` ID
    :>json datetime reserved_till: Related Legal
    :>json object rules: `Rules` mapping
    :>json string vendor: :ref:`vendor <partner>` ID
    :>json string status: Order status
    :>json array tickets: List of ordered `tickets` ids
    :>json datetime updated_at: Partner update timestamp
    :>json array promocodes: List of `promocode` as objects
    :>json value: Value
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        PATCH /v1/resources/orders/535fb19bdca6a9d1638f2007 HTTP/1.1
        Accept: application/json
        Content-Type: applcation/json
        Host: ticketscloud.org

        {
            "tickets": [
                "537df47b6ab04735203a7219",
                "53b9421428422ec1b9cafbb5",
                "734b22afa3d5283e7146734d7e97b158"
            ]
        }

    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "customer": {},
            "created_at": null,
            "deal": "535fb1f1dca6a9d1638f2008",
            "event": "5357baaff51600525c9e1397",
            "id": "537e1d95f05f951cded9cb02",
            "reserved_till": null,
            "rules": {
                "5360a75a2b590f1c88e8680c": "537368ff1b9bf9d05cca835a"
            },
            "vendor": null,
            "status": "executed",
            "tickets": [
                "537df47b6ab04735203a7219",
                "53b9421428422ec1b9cafbb5",
                "734b22afa3d5283e7146734d7e97b158"
            ],
            "updated_at": null,
            "value": null
        }

.. http:delete:: /v1/resources/orders/{idorder}
   :synopsis: Cancels order processing

    :<header Accept: :mimetype:`application/json`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        DELETE /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org

    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Length: 2
        Content-Type: application/json; charset=UTF-8
        Server: nginx

        {}


.. _api/resources/orders:

Orders
======

.. http:get:: /v1/resources/orders
    :synopsis: Returns list of orders

    :<header Accept: :mimetype:`application/json`
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr object customer: Customer information
    :>jsonarr datetime created_at: Partner creation timestamp
    :>jsonarr string deal: :ref:`deal` ID
    :>jsonarr string event: :ref:`event` ID
    :>jsonarr string id: :ref:`order` ID
    :>jsonarr datetime reserved_till: Related Legal
    :>jsonarr object rules: `Rules` mapping
    :>json string vendor: :ref:`vendor <partner>` ID
    :>jsonarr string status: Order status
    :>jsonarr array tickets: List of ordered `tickets` ids
    :>jsonarr datetime updated_at: Partner update timestamp
    :>json array promocodes: List of `promocode` as objects
    :>jsonarr value: Value
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


    **Request**:

    .. code-block:: http

        GET /v1/resources/orders HTTP/1.1
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
                "customer": {},
                "created_at": "2014-07-16T21:00:00+00:00",
                "deal": "535fb1f1dca6a9d1638f2008",
                "event": "5357baaff51600525c9e1397",
                "id": "537e1d95f05f951cded9cb02",
                "reserved_till": "2015-07-16T21:00:00+00:00",
                "rules": {
                    "5360a75a2b590f1c88e8680c": "537368ff1b9bf9d05cca835a"
                },
                "vendor": null,
                "status": "executed",
                "tickets": [
                    "53b9421428422ec1b9cafbb5",
                    "537df47b6ab04735203a7219"
                ],
                "updated_at": "2014-07-16T21:00:00+00:00",
                "value": null
            },
            {
                "customer": {
                    "email": null,
                    "first_name": null,
                    "last_name": null,
                    "user": null
                },
                "created_at": "2014-07-16T21:00:00+00:00",
                "deal": "535fb1f1dca6a9d1638f2008",
                "event": "5357baaff51600525c9e1397",
                "id": "5360a81f2b590f1c88e8680f",
                "reserved_till": null,
                "rules": {
                    "5360a75a2b590f1c88e8680c": "537368ff1b9bf9d05cca835a"
                },
                "vendor": null,
                "status": "done",
                "tickets": [
                    "5360a7fc2b590f1c88e8680e"
                ],
                "updated_at": "2014-07-16T21:00:00+00:00",
                "value": null
            }
        ]


Order Lifecycle
===============

.. code-block:: text

    +----------+     +-------------+     +------+     +----------+
    | executed | --> | in_progress | --> | done | --> | refunded |
    +----------+     +-------------+     +------+     +----------+
      |                |
      |                |
      v                |
    +----------+       |
    | canceled | <-----+
    +----------+


Order Creation
--------------

On order creation, you must specify the `ticket` IDs which customer wanted
to buy:

.. code-block:: http

    POST /v1/resources/orders HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "tickets": ["ticket-id1", "ticket-id2"],
        "event": "event-id"
    }

However, for some events there are no tickets which may have some specific
serial number or ID, or you don't even care about. In this cause you can order
just some "random" tickets without explicitly specifying their IDs:

.. code-block:: http

    POST /v1/resources/orders HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "random": {
            "ticketset-id": 13,
        }
        "event": "event-id"
    }

The :ref:`deal` ID is optional and only need when you have to explicitly define
the related deal which will be used for price calculation.

When order becomes created, it receives status `executed`.


Order updating
--------------

When order is created, the only information that could be updated is the
ordered tickets:

.. code-block:: text

    PATCH /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "tickets": ["id2", "id3"]
    }

.. code-block:: text

    PATCH /v1/resources/orders/{idorder} HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "random": {
            "ticketset-id": 13,
            "other-ticketset-id": 1,
        }
    }

You must to always pass full set of tickets that have to be in the order, even
if you want to add the single one onto it. If some tickets were ordered, but
becomes missed on update their reservation gets removed.


Order Commit
------------

When order is done and it's time to pay the money for it, it must be updated
to set status as `in_progress`:

.. code-block:: http

    PATCH /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "status": "in_progress"
    }


Order Completion
----------------

When order had been paid, it must be updated to set status as `done`:

.. code-block:: http

    PATCH /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "status": "done"
    }


Order Cancellation
------------------

However, sometime you'll have to cancel the order. This could be done with
easy by order deletion:

.. code-block:: http

    DELETE /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
    Authorization: key my-very-secret-key

This operation is equivalent to manually status update to `canceled`:

.. code-block:: http

    PATCH /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "status": "canceled"
    }


Update Customer Information
---------------------------

.. code-block:: http

    PATCH /v1/resources/orders/537e1d95f05f951cded9cb02 HTTP/1.1
    Authorization: key my-very-secret-key
    Content-Type: application/json

    {
        "customer": {
            "first_name": "John",
            "last_name": "Smith",
            "email": "user@mail.us",
        }
    }
