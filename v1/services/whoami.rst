.. _api/service/whoami:

Who Am I
========

.. http:post:: /v1/services/whoami
    :synopsis: Initiates user cookie session

    Initiates user cookie session.

    :<header Accept: :mimetype:`application/json`
    :<header Content-Type: :mimetype:`application/json`
    :<json string email: User email
    :<json string password: User password
    :>header Content-Type: :mimetype:`application/json`
    :>header Set-Cookie: Authorization token
    :>header Transfer-Encoding: ``chunked``
    :>json datetime created_at: User creation timestamp
    :>json string email: User email address
    :>json string first_name: User first name
    :>json string id: User unique ID
    :>json last_name: User last name
    :>json array partners: List of the Partners which users may operate with
    :>json array tags: List of the  associated tags
    :>json datetime updated_at: User update timestamp
    :code 200: Authentication passed
    :code 400: Invalid payload data
    :code 401: Invalid credentials provided

    **Request**:

    .. sourcecode:: http

        POST /v1/services/whoami HTTP/1.1
        Accept: application/json
        Content-Length: 49
        Content-Type: application/json; charset=utf-8
        Host: ticketscloud.org

        {
            "email": "user@domain.tld",
            "password": "s3cr1t"
        }


    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Encoding: gzip
        Content-Type: application/json; charset=UTF-8
        Server: nginx
        Set-Cookie: auth_tkt="FiYmQwNmIyMWNiMjU0!userid_type:b64unicode"; Path=/
        Set-Cookie: auth_tkt="FiYmQwNmIyMWNiMjU0!userid_type:b64unicode"; Domain=ticketscloud.org; Path=/
        Set-Cookie: auth_tkt="FiYmQwNmIyMWNiMjU0!userid_type:b64unicode"; Domain=.ticketscloud.org; Path=/
        Transfer-Encoding: chunked

        {
            "created_at": "2014-07-31T09:51:33.363000+00:00",
            "email": "user@domain.tld",
            "first_name": null,
            "id": "53da11a537abbd06b21cb254",
            "last_name": null,
            "partners": [],
            "tags": [],
            "updated_at": "2014-07-31T09:51:33.363000+00:00"
        }


.. http:get:: /v1/services/whoami
    :synopsis: Returns information about authenticated user

    Returns information about authenticated user.

    :<header Accept: :mimetype:`application/json`
    :<header Cookie: Authorization token
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
    :code 200: OK
    :code 401: Invalid credentials provided

    **Request**:

    .. sourcecode:: http

        GET /v1/services/whoami HTTP/1.1
        Accept: application/json
        Cookie: auth_tkt="FiYmQwNmIyMWNiMjU0!userid_type:b64unicode"; Domain=ticketscloud.org; Path=/
        Host: ticketscloud.org

    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Encoding: gzip
        Content-Type: application/json; charset=UTF-8
        Server: nginx
        Transfer-Encoding: chunked

        {
            "created_at": "2014-07-31T09:51:33.363000+00:00",
            "email": "user@domain.tld",
            "first_name": null,
            "id": "53da11a537abbd06b21cb254",
            "last_name": null,
            "partners": [],
            "tags": [],
            "updated_at": "2014-07-31T09:51:33.363000+00:00"
        }


.. http:delete:: /v1/services/whoami
    :synopsis: Closes user cookie session

    Closes user cookie session.

    :<header Accept: :mimetype:`application/json`
    :<header Cookie: Authorization token
    :>header Content-Type: :mimetype:`application/json`
    :>header Set-Cookie: Authorization token
    :>header Transfer-Encoding: ``chunked``
    :code 200: OK

    **Request**:

    .. sourcecode:: http

        DELETE /v1/services/whoami HTTP/1.1
        Accept: application/json
        Cookie: auth_tkt="FiYmQwNmIyMWNiMjU0!userid_type:b64unicode"; Domain=ticketscloud.org; Path=/
        Host: ticketscloud.org

    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Encoding: gzip
        Content-Type: application/json; charset=UTF-8
        Server: nginx
        Set-Cookie: auth_tkt=; Domain=.ticketscloud.org; Max-Age=0; Path=/; expires=Wed, 31-Dec-97 23:59:59 GMT
        Transfer-Encoding: chunked

        {}
