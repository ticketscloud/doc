============
Tickets Sets
============

.. _set:
.. _api/resources/set:

Tickets Set
===========

.. http:get:: /v1/resources/events/{idevent}/sets/{idset}
    :synopsis: Returns information about the set

    Returns information about the set.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json number amount: Amount tickets in set
    :>json number amount_vacant: Amount vacant tickets in set
    :>json datetime created_at: Set creation timestamp
    :>json string current_price: Current price for tickets in set
    :>json object current_rule: Current price calculation rule
    :>json datetime created_at: Set creation timestamp
    :>json string description: Long text description
    :>json string event: :ref:`Event` ID
    :>json string id: :ref:`set` ID
    :>json string name: Tickets Set short name
    :>json boolean removed: Deletion flag
    :>json arrray rule: List of rules
    :>json datetime updated_at: Set update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:patch:: /v1/resources/events/{idevent}/sets/{idset}
    :synopsis: Updates set information

    Updates set information.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json number amount: Amount tickets in set
    :<json string name: Tickets Set short name
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json number amount: Amount tickets in set
    :>json number amount_vacant: Amount vacant tickets in set
    :>json datetime created_at: Set creation timestamp
    :>json string current_price: Current price for tickets in set
    :>json object current_rule: Current price calculation rule
    :>json datetime created_at: Set creation timestamp
    :>json string description: Long text description
    :>json string event: :ref:`Event` ID
    :>json string id: :ref:`set` ID
    :>json string name: Tickets Set short name
    :>json boolean removed: Deletion flag
    :>json arrray rule: List of rules
    :>json datetime updated_at: Set update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:delete:: /v1/resources/events/{idevent}/sets/{idset}
    :synopsis: Deletes a set

    Deletes a set.

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idevent: :ref:`event` ID
    :param string idset: :ref:`set` ID
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. _api/resources/sets:

Tickets Sets
============

.. http:get:: /v1/resources/events/{idevent}/sets
    :synopsis: Returns list of existed sets

    Returns list of existed sets

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :query string filter: Custom filter
    :query string org: Filters sets by :ref:`Organizer <partner>` ID
    :query boolean removed: Whenever include removed sets
    :query string status: Filters sets by their status
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr number amount: Amount tickets in set
    :>jsonarr number amount_vacant: Amount vacant tickets in set
    :>jsonarr datetime created_at: Set creation timestamp
    :>jsonarr string current_price: Current price for tickets in set
    :>jsonarr object current_rule: Current price calculation rule
    :>jsonarr datetime created_at: Set creation timestamp
    :>jsonarr string description: Long text description
    :>jsonarr string event: :ref:`Event` ID
    :>jsonarr string id: :ref:`set` ID
    :>jsonarr string name: Tickets Set short name
    :>jsonarr boolean removed: Deletion flag
    :>jsonarr arrray rule: List of rules
    :>jsonarr datetime updated_at: Set update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:post:: /v1/resources/events/{idevent}/sets
    :synopsis: Creates a new set

    Creates a new set.

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json number amount: Amount tickets in set
    :<json string name: Tickets Set short name
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json number amount: Amount tickets in set
    :>json number amount_vacant: Amount vacant tickets in set
    :>json datetime created_at: Set creation timestamp
    :>json string current_price: Current price for tickets in set
    :>json object current_rule: Current price calculation rule
    :>json datetime created_at: Set creation timestamp
    :>json string description: Long text description
    :>json string event: :ref:`Event` ID
    :>json string id: :ref:`set` ID
    :>json string name: Tickets Set short name
    :>json boolean removed: Deletion flag
    :>json arrray rule: List of rules
    :>json datetime updated_at: Set update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed
