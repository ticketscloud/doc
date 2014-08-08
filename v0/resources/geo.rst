.. _api/geo:

========
Geo Data
========


.. _api/resources/countries:

Countries
=========

.. http:get:: /v0/resources/countries
    :synopsis: Returns list of countries

    Returns list of countries.

    :<header Accept: :mimetype:`application/json`
    :>header Content-Type: :mimetype:`application/json`
    :query string ids: List of object ids to return
    :query number limit: Limit returned collection by specified number
    :query number offset: Skip specified number of object from start
    :query string suggest: Asks to suggest the countries which contains
                           specified substring
    :query string fields-schema: :ref:`api/dsl`
    :>jsonarr string id: Country ID
    :>jsonarr object name: Mapping of locale to localized name
    :>jsonarr string type: Object type
    :code 200: OK

    **Request**:

    .. sourcecode:: http

        GET /v0/resources/countries HTTP/1.1
        Accept: application/json
        Host: ticketscloud.ru

    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "id": "AF",
                "name": {
                    "default": "Afghanistan",
                    "en": "Afghanistan"
                },
                "type": "country"
            },
            {
                "id": "AX",
                "name": {
                    "default": "Aland Islands",
                    "en": "Aland Islands"
                },
                "type": "country"
            },
            {
                "id": "AL",
                "name": {
                    "default": "Albania",
                    "en": "Albania"
                },
                "type": "country"
            },
            {
                "id": "DZ",
                "name": {
                    "default": "Algeria",
                    "en": "Algeria"
                },
                "type": "country"
            },
            {
                "id": "AS",
                "name": {
                    "default": "American Samoa",
                    "en": "American Samoa"
                },
                "type": "country"
            },
            {
                "id": "AD",
                "name": {
                    "default": "Andorra",
                    "en": "Andorra"
                },
                "type": "country"
            },
            {
                "id": "AO",
                "name": {
                    "default": "Angola",
                    "en": "Angola"
                },
                "type": "country"
            },
            {
                "id": "AI",
                "name": {
                    "default": "Anguilla",
                    "en": "Anguilla"
                },
                "type": "country"
            },
            {
                "id": "AQ",
                "name": {
                    "default": "Antarctica",
                    "en": "Antarctica"
                },
                "type": "country"
            },
            {
                "id": "AG",
                "name": {
                    "default": "Antigua and Barbuda",
                    "en": "Antigua and Barbuda"
                },
                "type": "country"
            },
            {
                "id": "AR",
                "name": {
                    "default": "Argentina",
                    "en": "Argentina"
                },
                "type": "country"
            },
            {
                "id": "AM",
                "name": {
                    "default": "Armenia",
                    "en": "Armenia"
                },
                "type": "country"
            },
            {
                "id": "AW",
                "name": {
                    "default": "Aruba",
                    "en": "Aruba"
                },
                "type": "country"
            },
            {
                "id": "AU",
                "name": {
                    "default": "Australia",
                    "en": "Australia"
                },
                "type": "country"
            },
            {
                "id": "AT",
                "name": {
                    "default": "Austria",
                    "en": "Austria"
                },
                "type": "country"
            },
            {
                "id": "AZ",
                "name": {
                    "default": "Azerbaijan",
                    "en": "Azerbaijan"
                },
                "type": "country"
            },
            {
                "id": "BS",
                "name": {
                    "default": "Bahamas",
                    "en": "Bahamas"
                },
                "type": "country"
            },
            {
                "id": "BH",
                "name": {
                    "default": "Bahrain",
                    "en": "Bahrain"
                },
                "type": "country"
            },
            {
                "id": "BD",
                "name": {
                    "default": "Bangladesh",
                    "en": "Bangladesh"
                },
                "type": "country"
            },
            {
                "id": "BB",
                "name": {
                    "default": "Barbados",
                    "en": "Barbados"
                },
                "type": "country"
            }
        ]

    When you don't really know which country you're looking for, you can pass
    `suggest` query parameter to filter alike countries by the specified name:

    **Request**:

    .. sourcecode:: http

        GET /v0/resources/countries?suggest=Rus HTTP/1.1
        Accept: application/json
        Host: ticketscloud.ru

    **Response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json; charset=UTF-8
        Transfer-Encoding: chunked

        [
            {
                "id": "RU",
                "name": {
                    "default": "Russia",
                    "en": "Russia"
                },
                "type": "country"
            }
        ]


.. _api/resources/cities:

Cities
======

.. http:get:: /v0/resources/cities
    :synopsis: Returns list of cities

    Returns list of cities.

    :<header Accept: :mimetype:`application/json`
    :>header Content-Type: :mimetype:`application/json`
    :query string ids: List of object ids to return
    :query number limit: Limit returned collection by specified number
    :query number offset: Skip specified number of object from start
    :query string suggest: Asks to suggest the countries which contains
                           specified substring
    :query string fields-schema: :ref:`api/dsl`
    :>jsonarr string country: Country ID
    :>jsonarr object id: City ID
    :>jsonarr object name: Mapping of locale to localized name
    :>jsonarr string timezone: Timezone in Olson database format
    :>jsonarr string type: Object type
    :code 200: OK

    **Request**:

    .. code-block:: http

        GET /v0/resources/cities HTTP/1.1
        Accept: application/json
        Host: ticketscloud.ru


    **Response**:

    .. code-block:: http

        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Type: application/json; charset=UTF-8
        Server: nginx
        Transfer-Encoding: chunked

        [
            {
                "country": "CN",
                "id": 1796236,
                "name": {
                    "default": "Shanghai",
                    "en": "Shanghai",
                    "fr": "Shanghai",
                    "ru": "Шанхай",
                    "zh": "中国上海"
                },
                "timezone": "Asia/Shanghai",
                "type": "city"
            },
            {
                "country": "AR",
                "id": 3435910,
                "name": {
                    "be": "Горад Буэнас-Айрэс",
                    "default": "Buenos Aires",
                    "en": "Buenos Aires",
                    "fr": "Buenos Aires",
                    "ru": "Буэнос-Айрес",
                    "zh": "布宜諾斯艾利斯"
                },
                "timezone": "America/Argentina/Buenos_Aires",
                "type": "city"
            },
            {
                "country": "IN",
                "id": 1275339,
                "name": {
                    "be": "Горад Мумбаі",
                    "default": "Mumbai",
                    "en": "Bombay",
                    "fr": "Bombay",
                    "ru": "Мумбаи"
                },
                "timezone": "Asia/Kolkata",
                "type": "city"
            },
            {
                "country": "MX",
                "id": 3530597,
                "name": {
                    "default": "Mexico City",
                    "en": "Mexico City",
                    "fr": "Mexico",
                    "ru": "Мехико",
                    "zh": "墨西哥城"
                },
                "timezone": "America/Mexico_City",
                "type": "city"
            },
            {
                "country": "PK",
                "id": 1174872,
                "name": {
                    "be": "Горад Карачы",
                    "default": "Karachi",
                    "en": "Karāchi",
                    "fr": "Karâchi",
                    "ru": "Карачи",
                    "zh": "喀拉蚩"
                },
                "timezone": "Asia/Karachi",
                "type": "city"
            },
            {
                "country": "TR",
                "id": 745044,
                "name": {
                    "default": "İstanbul",
                    "en": "Istanbul",
                    "fr": "Istanbul",
                    "ru": "Стамбул"
                },
                "timezone": "Europe/Istanbul",
                "type": "city"
            },
            {
                "country": "IN",
                "id": 1273294,
                "name": {
                    "be": "Горад Дэлі",
                    "default": "Delhi",
                    "en": "Delhi",
                    "fr": "Delhi",
                    "ru": "Дели",
                    "zh": "德里"
                },
                "timezone": "Asia/Kolkata",
                "type": "city"
            },
            {
                "country": "PH",
                "id": 1701668,
                "name": {
                    "be": "Горад Маніла",
                    "default": "Manila",
                    "en": "City of Manila",
                    "fr": "Manille",
                    "ru": "Манила"
                },
                "timezone": "Asia/Manila",
                "type": "city"
            },
            {
                "country": "RU",
                "id": 524901,
                "name": {
                    "be": "Горад Масква",
                    "default": "Moscow",
                    "en": "Moscow",
                    "fr": "Moscou",
                    "ru": "Москва",
                    "zh": "莫斯科"
                },
                "timezone": "Europe/Moscow",
                "type": "city"
            },
            {
                "country": "BD",
                "id": 1185241,
                "name": {
                    "be": "Горад Дака",
                    "default": "Dhaka",
                    "en": "Dhaka",
                    "fr": "Dacca",
                    "ru": "Дакка",
                    "zh": "达卡市"
                },
                "timezone": "Asia/Dhaka",
                "type": "city"
            },
            {
                "country": "KR",
                "id": 1835848,
                "name": {
                    "be": "Горад Сеул",
                    "default": "Seoul",
                    "en": "Seoul-si",
                    "fr": "Séoul",
                    "ru": "Сеул",
                    "zh": "首尔"
                },
                "timezone": "Asia/Seoul",
                "type": "city"
            },
            {
                "country": "BR",
                "id": 3448439,
                "name": {
                    "be": "Сан-Паўлу",
                    "default": "São Paulo",
                    "en": "São Paulo",
                    "fr": "São Paulo",
                    "ru": "Сан-Паулу"
                },
                "timezone": "America/Sao_Paulo",
                "type": "city"
            },
            {
                "country": "NG",
                "id": 2332459,
                "name": {
                    "be": "Горад Лагас",
                    "default": "Lagos",
                    "en": "Lagos",
                    "fr": "Lagos",
                    "ru": "Лагос",
                    "zh": "拉哥斯"
                },
                "timezone": "Africa/Lagos",
                "type": "city"
            },
            {
                "country": "ID",
                "id": 1642911,
                "name": {
                    "be": "Горад Джакарта",
                    "default": "Jakarta",
                    "en": "Jakarta",
                    "fr": "Jakarta",
                    "ru": "Джакарта",
                    "zh": "雅加达"
                },
                "timezone": "Asia/Jakarta",
                "type": "city"
            },
            {
                "country": "JP",
                "id": 1850147,
                "name": {
                    "default": "Tokyo",
                    "en": "Tokyo",
                    "fr": "Tokyo",
                    "ru": "Токио",
                    "zh": "東京都"
                },
                "timezone": "Asia/Tokyo",
                "type": "city"
            },
            {
                "country": "CN",
                "id": 1783873,
                "name": {
                    "default": "Zhumadian",
                    "en": "Zhumadian",
                    "fr": "Zhumadian",
                    "ru": "Чжумадянь"
                },
                "timezone": "Asia/Shanghai",
                "type": "city"
            },
            {
                "country": "US",
                "id": 5128581,
                "name": {
                    "be": "Нью-Ёрк",
                    "default": "New York City",
                    "en": "New York",
                    "fr": "New York",
                    "ru": "Нью-Йорк",
                    "zh": "纽约"
                },
                "timezone": "America/New_York",
                "type": "city"
            },
            {
                "country": "TW",
                "id": 1668341,
                "name": {
                    "default": "Taipei",
                    "en": "Taipei",
                    "fr": "Taipei",
                    "ru": "Тайбэй",
                    "zh": "臺北市"
                },
                "timezone": "Asia/Taipei",
                "type": "city"
            },
            {
                "country": "CD",
                "id": 2314302,
                "name": {
                    "be": "Горад Кіншаса",
                    "default": "Kinshasa",
                    "en": "Kinshasa",
                    "fr": "Kinshasa",
                    "ru": "Киншаса",
                    "zh": "金夏沙"
                },
                "timezone": "Africa/Kinshasa",
                "type": "city"
            },
            {
                "country": "PE",
                "id": 3936456,
                "name": {
                    "be": "Горад Ліма",
                    "default": "Lima",
                    "en": "Lima",
                    "fr": "Lima",
                    "ru": "Лима",
                    "zh": "利馬"
                },
                "timezone": "America/Lima",
                "type": "city"
            }
        ]
