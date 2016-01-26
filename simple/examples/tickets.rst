.. _ex/tickets:

/v1/resources/events/:id/tickets
================================

Запрос к event'у с метсами, возвращает информацию о сете, секторе и расположение метса в целом:

**Request**:

.. sourcecode:: http

    GET /v1/resources/events/56a6253df06c5a059a93802e/tickets HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 047bdb8bcee44d3693371920aaf9135c
    Content-Type: application/json
           
**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    X-Partner: 56810047f06c5a6ac62f4e1d

    [
        {
            "id": "56a6253df06c5a059a9380a0", 
            "reserved_till": null, 
            "seat": {
                "number": 1, 
                "row": 1, 
                "sector": "54d7a0409cb538783b7bf8d5"
            }, 
            "set": "56a6254bf06c5a059b93800c", 
            "status": "vacant"
        }, 
        {
            "id": "56a6253df06c5a059a9380a4", 
            "reserved_till": null, 
            "seat": {
                "number": 3, 
                "row": 1, 
                "sector": "54d7a0409cb538783b7bf8d5"
            }, 
            "set": "56a6254bf06c5a059b93800c", 
            "status": "vacant"
        }, 
        {
            "id": "56a6253df06c5a059a9380aa", 
            "reserved_till": null, 
            "seat": {
                "number": 6, 
                "row": 1, 
                "sector": "54d7a0409cb538783b7bf8d5"
            }, 
            "set": "56a6254bf06c5a059b93800c", 
            "status": "vacant"
        }
    ]
