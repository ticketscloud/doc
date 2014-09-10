======
Venues
======

.. _venue:
.. _api/resources/venue:

Venue
=====

.. http:get:: /v0/resources/venues/{idvenue}
    :synopsis: Returns information about the venue

    Returns information about the venue.

    :<header Accept: :mimetype:`application/json`
    :param string idvenue: :ref:`venue` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string address: Venue location address
    :>json number city: :ref:`City <api/resources/cities>` ID
    :>json string country: :ref:`Country <api/resources/countries>` ID
    :>json datetime created_at: Partner creation timestamp
    :>json string description: Long text description
    :>json string id: :ref:`venue` ID
    :>json string name: Venue short name
    :>json object point: GeoJSON point
    :>json boolean removed: Deletion flag
    :>json datetime updated_at: Partner update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:patch:: /v0/resources/venues/{idvenue}
    :synopsis: Updates venue information

    Updates venue information.

    :<header Accept: :mimetype:`application/json`
    :param string idvenue: :ref:`venue` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string address: Venue location address
    :<json number city: :ref:`City <api/resources/cities>` ID
    :<json string country: :ref:`Country <api/resources/countries>` ID
    :<json string description: Long text description
    :<json string id: :ref:`venue` ID
    :<json string name: Venue short name
    :<json object point: GeoJSON point
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string address: Venue location address
    :>json number city: :ref:`City <api/resources/cities>` ID
    :>json string country: :ref:`Country <api/resources/countries>` ID
    :>json datetime created_at: Venue creation timestamp
    :>json string description: Long text description
    :>json string id: :ref:`venue` ID
    :>json string name: Venue short name
    :>json object point: GeoJSON point
    :>json boolean removed: Deletion flag
    :>json datetime updated_at: Venue update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:delete:: /v0/resources/venues/{idvenue}
    :synopsis: Deletes a venue

    Deletes a venue.

    :<header Accept: :mimetype:`application/json`
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. _api/resources/venues:

Venues
======

.. http:get:: /v0/resources/venues
    :synopsis: Returns list of existed venues

    :<header Accept: :mimetype:`application/json`
    :param string idvenue: :ref:`venue` ID
    :query string fields-schema: :ref:`api/dsl`
    :query string filter: Custom filter
    :query string org: Filters venues by :ref:`Organizer <partner>` ID
    :query boolean removed: Whenever include removed venues
    :query string status: Filters venues by their status
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string address: Venue location address
    :>json number city: :ref:`City <api/resources/cities>` ID
    :>json string country: :ref:`Country <api/resources/countries>` ID
    :>json datetime created_at: Partner creation timestamp
    :>json string description: Long text description
    :>json string id: :ref:`venue` ID
    :>json string name: Venue short name
    :>json object point: GeoJSON point
    :>json boolean removed: Deletion flag
    :>json datetime updated_at: Partner update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:post:: /v0/resources/venues
    :synopsis: Creates a new venue

    Creates a new venue.

    :<header Accept: :mimetype:`application/json`
    :param string idvenue: :ref:`venue` ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string address: Venue location address
    :<json number city: :ref:`City <api/resources/cities>` ID
    :<json string country: :ref:`Country <api/resources/countries>` ID
    :<json string description: Long text description
    :<json string id: :ref:`venue` ID
    :<json string name: Venue short name
    :<json object point: GeoJSON point
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string address: Venue location address
    :>json number city: :ref:`City <api/resources/cities>` ID
    :>json string country: :ref:`Country <api/resources/countries>` ID
    :>json datetime created_at: Venue creation timestamp
    :>json string description: Long text description
    :>json string id: :ref:`venue` ID
    :>json string name: Venue short name
    :>json object point: GeoJSON point
    :>json boolean removed: Deletion flag
    :>json datetime updated_at: Venue update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed
