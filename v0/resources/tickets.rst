=======
Tickets
=======

.. _ticket:
.. _api/resources/ticket:

Ticket
======

.. http:get:: /v0/resources/events/{idevent}/sets/{idset}/tickets/{idticket}
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
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:patch:: /v0/resources/events/{idevent}/sets/{idset}/tickets/{idticket}
    :synopsis: Updates ticket information

    Updates ticket information.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :param string idticket: :ref:`ticket` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string status: Ticket status
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
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:delete:: /v0/resources/events/{idevent}/sets/{idset}/tickets/{idticket}
    :synopsis: Deletes a ticket

    Deletes a ticket.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :param string idticket: :ref:`ticket` ID
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. _api/resources/tickets:

Tickets
=======

.. http:get:: /v0/resources/tickets
    :synopsis: Returns list of existed tickets

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :param string idticket: :ref:`ticket` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr string barcode: Barcode (Code-128)
    :>jsonarr datetime created_at: Ticket creation timestamp
    :>jsonarr string id: :ref:`ticket` ID
    :>jsonarr number number: Number
    :>jsonarr boolean removed: Deletion flag
    :>jsonarr string serial: Serial
    :>jsonarr string set: :ref:`set` ID
    :>jsonarr string status: Ticket status
    :>jsonarr datetime updated_at: Ticket update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:post:: /v0/resources/tickets
    :synopsis: Creates a new ticket

    Creates a new ticket.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :param string idticket: :ref:`ticket` ID
    :query string fields-schema: :ref:`api/dsl`
    :>json number number: Number
    :>json string serial: Serial
    :>json string status: Ticket status
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
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed
