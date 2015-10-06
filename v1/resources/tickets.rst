=======
Tickets
=======

.. _ticket:
.. _api/resources/ticket:

Ticket
======

.. http:get:: /v1/resources/events/{idevent}/sets/{idset}/tickets/{idticket}
    :synopsis: Returns information about the ticket

    Returns information about the ticket.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :param string idticket: :ref:`ticket` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``

    :>json string barcode: Barcode (Code-128)
    :>json datetime created_at: Ticket creation timestamp
    :>json string id: :ref:`ticket` ID
    :>json number number: Number
    :>json boolean removed: Deletion flag
    :>json string serial: Serial
    :>json string set: :ref:`set` ID
    :>json string status: Ticket status
    :>json datetime updated_at: Ticket update timestamp
    :>json object seat: Information for seat

        - **map** (*ObjectId*) Map id
        - **sector** (*ObjectId*) Sector id
        - **row** (*int*) Row number
        - **number** (*int*) Seat number

    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. _api/resources/tickets:

Tickets
=======

.. http:get:: /v1/resources/events/{idevent}/tickets
    :synopsis: Returns list of existed tickets

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :param string idticket: :ref:`ticket` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``

    :>json string barcode: Barcode (Code-128)
    :>json datetime created_at: Ticket creation timestamp
    :>json string id: :ref:`ticket` ID
    :>json number number: Number
    :>json boolean removed: Deletion flag
    :>json string serial: Serial
    :>json string set: :ref:`set` ID
    :>json string status: Ticket status
    :>json datetime updated_at: Ticket update timestamp
    :>json object seat: Information for seat

        - **map** (*ObjectId*) Map id
        - **sector** (*ObjectId*) Sector id
        - **row** (*int*) Row number
        - **number** (*int*) Seat number

    :code 200: Ok
    :code 400: Invalid request parameters
    :code 403: Operation not allowed


Event's Tickets
===============

.. http:get:: /v1/resources/events/{idevent}/tickets
    :synopsis: Returns information about the all tickets in events

    Returns information about the all tickets in events.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string id: :ref:`ticket` ID
    :>json string status: Ticket status
    :>json string set: :ref:`set` ID
    :>json datetime reserved_till: Ticket reserved till timestamp
    :>json object seat: Information for seat

        - **map** (*ObjectId*) Map id
        - **sector** (*ObjectId*) Sector id
        - **row** (*int*) Row number
        - **number** (*int*) Seat number

    :code 200: Ok
    :code 400: Invalid request parameters
    :code 403: Operation not allowed
