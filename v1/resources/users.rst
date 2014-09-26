=====
Users
=====

.. _user:
.. _api/resources/users/id:

User
====

Users are represents the humans which works with TicketsCloud API: each has
own credentials and association. Users can only update their information,
create related :ref:`partners <partner>` and their :ref:`keys <apikey>`.

.. http:get:: /v1/resources/users/{iduser}
    :synopsis: Returns user information

    Returns information about user by the specified ID.

    :<header Accept: :mimetype:`application/json`
    :param string iduser: User ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: User creation timestamp
    :>json string email: User email address
    :>json string first_name: User first name
    :>json string id: User unique ID
    :>json last_name: User last name
    :>json array partners: List of the Partners which users may operate with
    :>json array tags: List of the  associated tags
    :>json datetime updated_at: User update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/users/53e241d137abbd588116ef3e HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 Ok
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "created_at": "2014-08-06T14:55:13.601000+00:00",
            "email": "user@domain.ltd",
            "first_name": null,
            "id": "53e241d137abbd588116ef3e",
            "last_name": null,
            "partners": [],
            "tags": [],
            "updated_at": "2014-08-06T14:55:13.601000+00:00"
        }


.. http:patch:: /v1/resources/users/{iduser}
    :synopsis: Updates user information

    Updates user information.

    :<header Accept: :mimetype:`application/json`
    :param string iduser: User ID
    :query string fields-schema: :ref:`api/dsl`
    :<json string email: User email address
    :<json string first_name: User first name
    :<json last_name: User last name
    :<json password: New password
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: User creation timestamp
    :>json string email: User email address
    :>json string first_name: User first name
    :>json string id: User unique ID
    :>json last_name: User last name
    :>json array partners: List of the Partners which users may operate with
    :>json array tags: List of the  associated tags
    :>json datetime updated_at: User update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        PATCH /v1/resources/users/53da11a537abbd06b21cb254 HTTP/1.1
        Accept: application/json
        Content-Length: 45
        Cookie: auth_tkt="FiYmQwNmIyMWNiMjU0!userid_type:b64unicode"; Domain=ticketscloud.org; Path=/
        Host: ticketscloud.org

        {"last_name": "Smith", "first_name": "John"}

    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "created_at": "2014-07-31T09:51:33.363000+00:00",
            "email": "user@domain.tld",
            "first_name": "John",
            "id": "53da11a537abbd06b21cb254",
            "last_name": "Smith",
            "partners": [],
            "tags": [],
            "updated_at": "2014-07-31T09:51:33.363000+00:00"
        }


.. _api/resources/users:

Users
=====

Collection of :ref:`user` objects.

.. http:get:: /v1/resources/users
    :synopsis: Returns list of existed users

    Returns list of existed :ref:`users <user>`.

    :<header Accept: :mimetype:`application/json`
    :query string fields-schema: :ref:`api/dsl`
    :query string ids: Comma-separated ids to filter by
    :query boolean removed: Include deleted objects when ``true``
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr datetime created_at: User creation timestamp
    :>jsonarr string email: User email address
    :>jsonarr string first_name: User first name
    :>jsonarr string id: User unique ID
    :>jsonarr last_name: User last name
    :>jsonarr array partners: List of the Partners which users may operate with
    :>jsonarr array tags: List of the  associated tags
    :>jsonarr datetime updated_at: User update timestamp
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/users HTTP/1.1
        Accept: application/json
        Host: ticketscloud.org


    **Response**:

    .. code-block:: http

        HTTP/1.1 201 Created
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "created_at": "2014-08-06T14:55:13.601000+00:00",
                "email": "user@domain.ltd",
                "first_name": null,
                "id": "53e241d137abbd588116ef3e",
                "last_name": null,
                "partners": [],
                "tags": [],
                "updated_at": "2014-08-06T14:55:13.601000+00:00"
            },
            {
                "created_at": "2014-08-06T14:56:46.465000+00:00",
                "email": "user@domain.com",
                "first_name": null,
                "id": "53e2422e37abbd588116ef3f",
                "last_name": null,
                "partners": [],
                "tags": [],
                "updated_at": "2014-08-06T14:56:46.465000+00:00"
            },
            {
                "created_at": "2014-08-06T14:57:13.577000+00:00",
                "email": "user@domain.net",
                "first_name": null,
                "id": "53e2424937abbd587e16ef3e",
                "last_name": null,
                "partners": [],
                "tags": [],
                "updated_at": "2014-08-06T14:57:13.577000+00:00"
            },
            {
                "created_at": "2014-08-06T14:58:49.489000+00:00",
                "email": "user@domain.org",
                "first_name": null,
                "id": "53e242a937abbd588116ef40",
                "last_name": null,
                "partners": [],
                "tags": [],
                "updated_at": "2014-08-06T14:58:49.489000+00:00"
            }
        ]


.. http:post:: /v1/resources/users
    :synopsis: Registers a new user

    Registers a new :ref:`user <user>`.

    :<header Accept: :mimetype:`application/json`
    :<header Content-Type: :mimetype:`application/json`
    :query string fields-schema: :ref:`api/dsl`
    :<json string email: User email
    :<json string password: User password
    :>header Content-Type: :mimetype:`application/json`
    :>json datetime created_at: User creation timestamp
    :>json string email: User email address
    :>json string id: User unique ID
    :>json array partners: List of the Partners which users may operate with
    :>json array tags: List of the  associated tags
    :>json datetime updated_at: User update timestamp
    :code 201: User have been created
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        POST /v1/resources/users HTTP/1.1
        Accept: application/json
        Content-Length: 48
        Host: ticketscloud.org

        {
            "email": "user@domain.tld",
            "password": "s3cr1t"
        }


    **Response**:

    .. code-block:: http

        HTTP/1.1 201 Created
        Content-Length: 190
        Content-Type: application/json; charset=UTF-8

        {
            "created_at": "2014-08-06T14:59:20.323853+00:00",
            "email": "user@domain.tld",
            "id": "53e242c837abbd588116ef41",
            "partners": [],
            "tags": [],
            "updated_at": "2014-08-06T14:59:20.323853+00:00"
        }
