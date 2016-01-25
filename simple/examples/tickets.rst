.. _ex/tickets:

/v1/resources/events/:id/tickets
================================

Запрос к event'у с метсами, возвращает информацию о сете, секторе и расположение метса в целом:

**Request**:

.. code:: html

    GET http://ticketscloud.org/v1/resources/events/56a6253df06c5a059a93802e/tickets
    Authorization: key 047bdb8bcee44d3693371920aaf9135c
    Accept: application/json
    Content-Type: application/json
           

.. code:: html

    [
      {
        "id": "56a6253df06c5a059a9380a0",
        "set": "56a6254bf06c5a059b93800c",
        "seat": {
          "row": 1,
          "number": 1,
          "sector": "54d7a0409cb538783b7bf8d5"
        },
        "reserved_till": null,
        "status": "vacant"
      },
      {
        "id": "56a6253df06c5a059a9380a4",
        "set": "56a6254bf06c5a059b93800c",
        "seat": {
          "row": 1,
          "number": 3,
          "sector": "54d7a0409cb538783b7bf8d5"
        },
        "reserved_till": null,
        "status": "vacant"
      },
      {
        "id": "56a6253df06c5a059a9380aa",
        "set": "56a6254bf06c5a059b93800c",
        "seat": {
          "row": 1,
          "number": 6,
          "sector": "54d7a0409cb538783b7bf8d5"
        },
        "reserved_till": null,
        "status": "vacant"
      }
    ]
    // GET http://ticketscloud.org/v1/resources/events/56a6253df06c5a059a93802e/tickets
    // HTTP/1.1 200 OK
    // Server: nginx/1.8.0
    // Date: Mon, 25 Jan 2016 13:38:40 GMT
    // Content-Type: application/json; charset=UTF-8
    // Content-Length: 555
    // Connection: keep-alive
    // X-Partner: 56810047f06c5a6ac62f4e1d
    // Cache-Control: private, max-age=0, no-cache, no-store
    // Request duration: 0.259888s
