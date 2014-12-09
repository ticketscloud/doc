==========
Promocodes
==========

.. promocode:
.. _api/resources/promocode:

Promocodes
==========

.. http:get:: /v1/resources/events/{event_id}/promocodes/{promocode_id}
    :synopsis: Returns information about the promocode

    Returns information about the promocode

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string event_id: :ref:`event` ID
    :param string promocode_id: :ref:`promocode` ID
    :query string fields-schema: :ref:`api/dsl`

    :<json arrray sets: List of ticketsets
    :<json string name: Name of promocode
    :<json string desc: Descriprion of promocode
    :<json dict discount: discount value (`percengate` or `fixed` keys)
    :<json number amount: amount of promocode uses
    :<json string code: Code for users
    :<json string lifetime:

    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: Set creation timestamp
    :>json datetime updated_at: Set update timestamp
    :>json string event: :ref:`event` ID
    :>json arrray sets: List of ticketsets
    :>json string name: Name of promocode
    :>json string desc: Descriprion of promocode
    :>json dict discount: discount value `percengate` or `fixed`
    :>json number amount: amount of promocode uses
    :>json string code: Code for users
    :>json string lifetime:
    :>json dict counter: promocode usage information

    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:post:: /v1/resources/events/{event_id}/promocodes
    :synopsis: Create promocode

    Create promocode

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string promocode_id: :ref:`promocode` ID
    :query string fields-schema: :ref:`api/dsl`

    :<json arrray sets: List of ticketsets
    :<json string name: Name of promocode
    :<json string desc: Descriprion of promocode
    :<json dict discount: discount value (`percengate` or `fixed` keys)
    :<json number amount: amount of promocode uses
    :<json string code: Code for users
    :<json string lifetime:

    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: Set creation timestamp
    :>json datetime updated_at: Set update timestamp
    :>json string event: :ref:`event` ID
    :>json arrray sets: List of ticketsets
    :>json string name: Name of promocode
    :>json string desc: Descriprion of promocode
    :>json dict discount: discount value `percengate` or `fixed`
    :>json number amount: amount of promocode uses
    :>json string code: Code for users
    :>json string lifetime:
    :>json dict counter: promocode usage information

    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


.. http:patch:: /v1/resources/events/{event_id}/promocodes/{promocode_id}
    :synopsis: Edit promocode

    Edit promocode

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string event_id: :ref:`event` ID
    :param string promocode_id: :ref:`promocode` ID
    :query string fields-schema: :ref:`api/dsl`

    :<json string name: Name of promocode
    :<json string desc: Descriprion of promocode

    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: Set creation timestamp
    :>json datetime updated_at: Set update timestamp
    :>json string event: :ref:`event` ID
    :>json arrray sets: List of ticketsets
    :>json string name: Name of promocode
    :>json string desc: Descriprion of promocode
    :>json dict discount: discount value `percengate` or `fixed`
    :>json number amount: amount of promocode uses
    :>json string code: Code for users
    :>json string lifetime:
    :>json dict counter: promocode usage information

    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed
