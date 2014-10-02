===========
Media Files
===========

.. _att:
.. _api/resources/attachments:

Attachment
==========

.. http:get:: /v1/resources/attachment/{idatt}
    :synopsis: Return information about a stored file

    :<header Accept: :mimetype:`application/json`
    :<header Authorization: :ref:`API key <apikey>`
    :param string idatt: :ref:`att` ID
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>json string author: :ref:`partner` ID
    :>json string content_type: MIME type
    :>json datetime created_at: File creation timestamp
    :>json string id: :ref:`att` ID
    :>json number length: File content length
    :>json string md5: MD5 hash from file`s content
    :>json datetime updated_at: File update timestamp
    :>json string url: Direct URL to the file
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed


    **Request**:

    .. code-block:: http

        GET /v1/resources/attachments/53f1d8ab9437bdca80a97882 HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Host: ticketscloud.org

    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "author": "8ab53f1d94dca37b8088a972",
            "content_type": "image/gif",
            "created_at": "2014-10-02T10:42:28.288000+00:00",
            "id": "53f1d8ab9437bdca80a97882",
            "length": 4201,
            "md5": "bfd55d7efd971d30d1b429cfebde0b71",
            "removed": false,
            "updated_at": "2014-10-02T10:42:28.288000+00:00"
        }



.. _api/resources/attachment:

Attachments
===========

.. http:get:: /v1/resources/attachments
    :synopsis: Returns list of active deals

    :<header Accept: :mimetype:`application/json`
    :query string fields-schema: :ref:`api/dsl`
    :>header Content-Type: :mimetype:`application/json`
    :>header Transfer-Encoding: ``chunked``
    :>jsonarr string author: :ref:`partner` ID
    :>jsonarr string content_type: MIME type
    :>jsonarr datetime created_at: File creation timestamp
    :>jsonarr string id: :ref:`att` ID
    :>jsonarr number length: File content length
    :>jsonarr string md5: MD5 hash from file`s content
    :>jsonarr datetime updated_at: File update timestamp
    :>jsonarr string url: Direct URL to the file
    :code 200: Ok
    :code 400: Invalid request parameters
    :code 401: Authentication required
    :code 403: Operation not allowed

    **Request**:

    .. code-block:: http

        GET /v1/resources/attachments HTTP/1.1
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
                "author": "8ab53f1d94dca37b8088a972",
                "content_type": "image/gif",
                "created_at": "2014-10-02T10:42:28.288000+00:00",
                "id": "53f1d8ab9437bdca80a97882",
                "length": 4201,
                "md5": "bfd55d7efd971d30d1b429cfebde0b71",
                "removed": false,
                "updated_at": "2014-10-02T10:42:28.288000+00:00"
            }
        ]



.. http:post:: /v1/resources/attachments
    :synopsis: Creates a new file

    Creates a new file.

    :<header Accept: :mimetype:`application/json`
    :param string idevent: :ref:`event` ID
    :query string fields-schema: :ref:`api/dsl`
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


    **Request**:

    .. code-block:: http

        POST /v1/resources/attachments HTTP/1.1
        Accept: application/json
        Authorization: key my-very-secret-key
        Content-Length: 4201
        Content-Type: image/gif
        Host: ticketscloud.org

        <...data...>


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        {
            "author": "8ab53f1d94dca37b8088a972",
            "content_type": "image/gif",
            "created_at": "2014-10-02T10:42:28.288000+00:00",
            "id": "53f1d8ab9437bdca80a97882",
            "length": 4201,
            "md5": "bfd55d7efd971d30d1b429cfebde0b71",
            "removed": false,
            "updated_at": "2014-10-02T10:42:28.288000+00:00"
        }
