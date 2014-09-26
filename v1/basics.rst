.. _api/basics:

==========
API Basics
==========

In this chapter you'll find HTTP API common bits about design and workflow.


.. _api/http:

HTTP Basics
===========

TicketsCloud API is based on HTTP, so it would be good for you to know it
basics at the first place. We wouldn't copy-paste whole :rfc:`2616`
and it `recent updates <http://evertpot.com/http-11-updated/>`_ there. Instead,
we strongly RECOMMEND you to ackowledge with them. Above we'll describe only
parts of HTTP specification which TicketsCloud API is widely uses.


Request Methods
---------------

TicketsCloud uses the following HTTP request methods:

- :method:`GET`

    Request the specified item.

- :method:`HEAD`

    This method works like :method:`GET` except that request with it doesn't
    returns payload content.

- :method:`POST`

   Create a new object or makes some action that doesn't creates a new resource.

- :method:`PUT`

   Used to update a specified resource or create a new one on the specified
   resource.

- :method:`DELETE`

    Deletes the specified resource, destroys associated object or cancels some
    action.

- :method:`PATCH`

    While :method:`PUT` is used to update whole resource content,
    :method:`PATCH` allows to update only certain fields without need to pass
    around all the data.


Request Headers
---------------

- :header:`Accept`

    Specifies the list of accepted data types to be returned by the
    server (i.e. that are accepted/understandable by the client). The
    format should be a list of one or more MIME types, separated by
    colons.

    For the majority of requests the definition should be for JSON data
    (:mimetype:`application/json`).

    The use of :mimetype:`Accept` in requests is not required, but is
    highly recommended as it helps to ensure that the data returned can
    be processed by the client.

    If resource is unable to return the response in the accepted MIME type,
    the :statuscode:`406` response will be returned instead.

- :header:`Authorization`

    Specified authentication token by which the server can recognize the related
    user.

    TicketsCloud API uses custom authentication scheme named ``Key``
    and custom unique token which users receives from TicketsCloud customers
    service.

    .. code-block:: http

        GET /v1/resources/events HTTP/1.1
        Accept: application/json
        Authorization: Key 6e6124cfc954496a850aa959ef2f64fa
        Host: ticketscloud.org

- :header:`Content-Type`

    Specifies the content type of the information being supplied within
    the request. The specification uses MIME type specifications. For the
    majority of requests this will be JSON (:mimetype:`application/json`).

    The use of the :header:`Content-Type` on a request is highly recommended.


Response Status Codes
---------------------

With the interface to CouchDB working through HTTP, error codes and
statuses are reported using a combination of the HTTP status code
number, and corresponding data in the body of the response data.

A list of the error codes returned by CouchDB, and generic descriptions
of the related errors are provided below. The meaning of different
status codes for specific request types are provided in the
corresponding API call reference.

- :statuscode:`200`

    Request completed successfully.

- :statuscode:`201`

    Resource object had been created successfully.

- :statuscode:`202`

    Request has been accepted, but the corresponding operation may not
    have completed. This is used for background operations, such as
    database compaction.

- :statuscode:`400`

    Bad request structure. The error can indicate an error with the
    request URL, path, headers or payload data.

- :statuscode:`401`

    The item requested was not available using the supplied
    authorization, or authorization was not supplied.

- :statuscode:`403`

    The requested item or operation is forbidden.

- :statuscode:`404`

    The requested content could not be found. The content will include
    further information, as a JSON object, if available.

- :statuscode:`405`

    A request was made using an invalid HTTP request type for the URL
    requested. For example, you have requested a :method:`PUT` when a
    :method:`POST` is required. Errors of this type can also triggered
    by invalid URL strings.

- :statuscode:`406`

    The requested content type is not supported by the server.

- :statuscode:`409`

    Request resulted in an update conflict.

- :statuscode:`415`

    The content types supported, and the content type of the information
    being requested or submitted indicate that the content type is not
    supported.

- :statuscode:`500`

    The request was invalid, either because the supplied JSON was
    invalid, or invalid information was supplied as part of the request.

- :statuscode:`502`

    Something really gone wrong.


Response Headers
----------------

Response headers are returned by the server when sending back content
and include a number of different header fields, many of which are
standard HTTP response header and have no significance to CouchDB
operation. The list of response headers important to CouchDB are listed
below.

- :header:`Content-Length`

    The length (in bytes) of the returned content.

- :header:`Content-Type`

    Specifies the MIME type of the returned data. For most request, the
    returned MIME type is :mimetype:`text/plain`. All text is encoded in Unicode
    (UTF-8), and this is explicitly stated in the returned
    :header:`Content-Type`, as :mimetype:`text/plain;charset=utf-8`.

- :header:`Cache-Control`

    The cache control HTTP response header provides a suggestion for
    client caching mechanisms on how to treat the returned information.
    CouchDB typically returns the ``must-revalidate``, which indicates
    that the information should be revalidated if possible. This is used
    to ensure that the dynamic nature of the content is correctly
    updated.


.. _api/version:

Versioning
==========

TicketsCloud HTTP API is versioned by using URL approach: the version is
explicitly defined as path segment in the format ``v<num>``. Version numeration
is stated from ``1`` and grows one by one.

Within the same version we guarantee that everything will works as it was
before.

In case of breaking changes in API, version number gets bumped.


.. _api/json:

JSON
====

The majority of requests and responses to TicketsCloud API uses the JavaScript
Object Notation (`JSON <http://json.org/>`_) for formatting the content and
structure of the data and responses.

JSON is used because it is the simplest and easiest to use solution for
working with data within a web browser, as JSON structures can be
evaluated and used as JavaScript objects within the web browser
environment.

JSON supports the same basic types as supported by JavaScript, these
are:

-   Number (either integer or floating-point).

-   String; this should be enclosed by double-quotes and supports Unicode
    characters and backslash escaping. For example:

   .. code-block:: javascript

       "A String"

-   Boolean - a ``true`` or ``false`` value. You can use these strings
    directly. For example:

   .. code-block:: javascript

       true

-   Array - a list of values enclosed in square brackets. For example:

   .. code-block:: javascript

       ["one", "two", "three"]

-   Object - a set of key/value pairs (i.e. an associative array, or
    hash). The key must be a string, but the value can be any of the
    supported JSON values.

Parsing JSON into a JavaScript object is supported through the ``JSON.parse()``
function in JavaScript, or through various libraries that will perform
the parsing of the content into a JavaScript object for you. Libraries for
parsing and generating JSON are available in many languages, including Perl,
Python, Ruby, Erlang and others.


.. _api/dsl:

Fields Schema DSL
=================

When we made a request to some resource, in most cases we don't want all the
data, just a small part of it. We receiving JSON object, picking the fields
we're interested in leaving every else for garbage collector.

TicketsCloud API provides a feature to receive only those fields you're
using special query parameter `fields-schema`. It accepts the special DSL
value which uses as field filter on server side, returning an object with only
specified fields.

For example, we need to receive our current user ID and email fields only:

**Request**:

.. sourcecode:: http

    GET /v1/services/whoami?fields-schema=id,email HTTP/1.1
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
        "id": "53da11a537abbd06b21cb254",
        "email": "user@domain.tld"
    }

You may freely specify any top level fields separated by comma as
`fields-schema` value. In case if the value is incorrect, a :statuscode:`400`
response will be returned.
