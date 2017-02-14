.. _ex/refund:

Возврат билетов
===============

Для возврата нам потребуется :ref:`заказ <simple/orders/create>`
в статусе :ref:`done`, его ``id``, список ``id`` билетов из этого заказа,
которые надо вернуть и виновник.

Допустим покупатель решил вернуть два билета из заказа.

Создаем :ref:`запрос на возврат <simple/refund>`:

**Request**:

.. sourcecode:: http

    POST /v1/resources/refund_requests HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 968cd37341029c26d173b1113f0002cd
    Content-Type: application/json

    {
        "culprit": "user",
        "order": "5703d7542d709509727f929c",
        "tickets_refund": [
            "56ba2b6f9cb53851972a28db",
            "56ba2b6f9cb53851972a2883"
        ]
    }


**Response**:

.. sourcecode:: http

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8
    X-Partner: 54bcf9269cb53859759321c8

    {
        "created_at": "2016-04-05T15:34:02.502481+00:00",
        "culprit": "user",
        "id": "5703daea2d709509727f92a5",
        "order": "5703d7542d709509727f929c",
        "org": "54bcf9269cb538597597b5c8",
        "payment_system": "545b544a5d645a463e779d53",
        "status": "new",
        "tickets_refund": [
            "56ba2b6f9cb53851972a28db",
            "56ba2b6f9cb53851972a2883"
        ],
        "tickets": [],
        "updated_at": "2016-04-05T15:34:02.502481+00:00",
        "value": "0.00",
        "vendor": "54bcf9269c3248597597b5c8"
    }

После успешного создания запроса на возрат мы можем подтвердить его.
Для этого нам понадобится только ``id`` :ref:`запроса на возврат <simple/refund>`.

**Request**:

.. sourcecode:: http

    PATCH /v1/resources/refund_requests/5703daea2d709509727f92a5 HTTP/1.1
    Host: api.ticketscloud.org
    Accept: application/json
    Authorization:  key 968cd37341029c26d173b1113f0002cd
    Content-Type: application/json

    {
        "status": "approved"
    }


**Response**:

.. sourcecode:: http

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8
    X-Partner: 54bcf9269cb53859759321c8

    {
        "created_at": "2016-04-05T15:41:10.130000+00:00",
        "culprit": "user",
        "id": "5703daea2d709509727f92a5",
        "order": "5703d7542d709509727f929c",
        "org": "54bcf9269cb538597597b5c8",
        "payment_system": "545b544a5d645a463e779d53",
        "status": "approved",
        "tickets_refund": [
            "56ba2b6f9cb53851972a28db",
            "56ba2b6f9cb53851972a2883"
        ],
        "tickets": [],
        "updated_at": "2016-04-05T15:41:10.130000+00:00",
        "value": "0.00",
        "vendor": "54bcf9269c3248597597b5c8"
    }


После успешного подтверждения :ref:`запроса на возврат <simple/refund>`
деньги будут возвращениы в соответствии с логикой системы.
