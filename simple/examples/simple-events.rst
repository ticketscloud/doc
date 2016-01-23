.. _ex/simple-events:

/v1/services/simple/events
==========================

**Request**:

.. sourcecode:: http

    GET /v1/services/simple/events HTTP/1.1
    Accept: application/json
    Content-Type: application/json
    Host: ticketscloud.org
    Authorization: key 0123456789abcdef0123456789abcdef

**Response**:

.. sourcecode:: http

    HTTP/1.1 200 OK
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json; charset=UTF-8
    Server: nginx
    Transfer-Encoding: chunked

    [
        {
            "age_rating": 0,
            "created_at": "2015-12-04T17:47:42.608000+00:00",
            "deal": null,
            "id": "5661d1be9cb53846e5d882d7",
            "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160124T160000Z\r\nDTEND;VALUE=DATE-TIME:20160124T173000Z\r\nEND:VEVENT\r\n",
            "map": null,
            "media": {
                "cover": {
                    "author": "55faee509cb5381f937a0274",
                    "content_type": "image/jpeg",
                    "id": "5661d1c29cb5384f16d8730f",
                    "length": 530281,
                    "md5hash": "ca48425906eaae24d6f8a95c68e8bd60",
                    "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/image/2015-12/5661d1c29cb5384f16d8730f.jpeg"
                },
                "cover_original": {
                    "author": "55faee509cb5381f937a0274",
                    "content_type": "image/jpeg",
                    "id": "5661d1c29cb5385800d86bcb",
                    "length": 1890089,
                    "md5hash": "f1aee7218e9630c60a51f442f75883b7",
                    "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/image/2015-12/5661d1c29cb5385800d86bcb.jpeg"
                },
                "cover_small": {
                    "author": "55faee509cb5381f937a0274",
                    "content_type": "image/jpeg",
                    "id": "5661d1c09cb53850eed87f52",
                    "length": 26974,
                    "md5hash": "8a680c65fe7a5761959b269c5d369d95",
                    "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/image/2015-12/5661d1c09cb53850eed87f52.jpeg"
                }
            },
            "org": {
                "contact": {
                    "address": "3-й Хорошевский проезд д.8 кв. 25",
                    "email": "collegiummusicum@icloud.com",
                    "name": "",
                    "phones": [
                        "89263019362"
                    ],
                    "www": "http://www.collegiummusicum.ru"
                },
                "desc": "Агентство Collegium Musicum ведёт активную концертную и духовно-просветительскую деятельность с 2008 года. Его название восходит к музыкальным обществам эпохи Барокко. Старинные collegii musicae регулярно собирались для исполнения и обсуждения вокальных и инструментальных произведений, объединяя музыкантов-профессионалов, творческую молодёжь и любителей искусства.Основные задачи Collegium Musicum:· популяризация мирового классического музыкального наследия (с акцентом на духовные произведения);· просвещение аудитории посредством классической музыки и расширение круга её слушателей;· поддержка молодых российских исполнителей;· привлечение студентов музыкальных учебных заведений к концертной практике.В концертах Кафедрального собора святых Петра и Павла звучит немецкий романтический орган, созданный в 1898 году и обладающий богатейшей звуковой палитрой. На этом уникальном историческом инструменте, являющемся гордостью собора, играют только лучшие органисты.Collegium Musicum ориентируется на самую взыскательную публику разных поколений и сотрудничает с высокопрофессиональными коллективами и солистами.",
                "id": "55faee509cb5381f937a0274",
                "media": {
                    "logo": {
                        "author": "55faee509cb5381f937a0274",
                        "content_type": "image/png",
                        "id": "55faee509cb5382f4f79e9d9",
                        "length": 17126,
                        "md5hash": "7b3e730fed27a753b30a287bb25cc92e",
                        "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/image/2015-09/55faee509cb5382f4f79e9d9.png"
                    },
                    "logo_original": {
                        "author": "55faee509cb5381f937a0274",
                        "content_type": "image/jpeg",
                        "id": "55faee509cb5385a047a25ef",
                        "length": 24311,
                        "md5hash": "e6648781a735d452af71e5814aee810c",
                        "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/image/2015-09/55faee509cb5385a047a25ef.jpe"
                    },
                    "logo_small": {
                        "author": "55faee509cb5381f937a0274",
                        "content_type": "image/png",
                        "id": "55faee509cb5382f4f79e9da",
                        "length": 37608,
                        "md5hash": "43e2ebd6551654f713b7f38d8b874ed0",
                        "url": "https://s3-eu-west-1.amazonaws.com:443/media.ticketscloud/production/image/2015-09/55faee509cb5382f4f79e9da.png"
                    }
                },
                "name": "Collegium Musicum",
                "tags": []
            },
            "sets": [
                {
                    "amount": 30,
                    "amount_vacant": 14,
                    "id": "5661d2679cb5384f16d873dd",
                    "name": "Льготный",
                    "pos": 0,
                    "price": "700.00",
                    "price_extra": "0.00",
                    "price_org": "700.00",
                    "rules": [
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20151203T210000Z\r\nDTEND;VALUE=DATE-TIME:20151223T205900Z\r\nEND:VEVENT\r\n",
                            "current": false,
                            "id": "5661d2679cb5384f16d873d7",
                            "price": "500.00",
                            "price_extra": "0.00",
                            "price_org": "500.00"
                        },
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20151223T210000Z\r\nDTEND;VALUE=DATE-TIME:20160108T205900Z\r\nEND:VEVENT\r\n",
                            "current": false,
                            "id": "5661d2679cb5384f16d873d8",
                            "price": "600.00",
                            "price_extra": "0.00",
                            "price_org": "600.00"
                        },
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160108T210000Z\r\nDTEND;VALUE=DATE-TIME:20160124T173000Z\r\nEND:VEVENT\r\n",
                            "current": true,
                            "id": "5661d2679cb5384f16d873d9",
                            "price": "700.00",
                            "price_extra": "0.00",
                            "price_org": "700.00"
                        }
                    ],
                    "seats": null,
                    "sector": null
                },
                {
                    "amount": 100,
                    "amount_vacant": 95,
                    "id": "5661d2fc9cb5385800d87215",
                    "name": "Партер 11-21 ряд (свободная рассадка)",
                    "pos": 0,
                    "price": "1020.00",
                    "price_extra": "0.00",
                    "price_org": "1020.00",
                    "rules": [
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20151203T210000Z\r\nDTEND;VALUE=DATE-TIME:20151223T205900Z\r\nEND:VEVENT\r\n",
                            "current": false,
                            "id": "5661d2fc9cb5385800d8720d",
                            "price": "600.00",
                            "price_extra": "0.00",
                            "price_org": "600.00"
                        },
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20151223T210000Z\r\nDTEND;VALUE=DATE-TIME:20160109T205900Z\r\nEND:VEVENT\r\n",
                            "current": false,
                            "id": "5661d2fc9cb5385800d8720e",
                            "price": "840.00",
                            "price_extra": "0.00",
                            "price_org": "840.00"
                        },
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160109T210000Z\r\nDTEND;VALUE=DATE-TIME:20160123T205900Z\r\nEND:VEVENT\r\n",
                            "current": true,
                            "id": "5661d2fc9cb5385800d8720f",
                            "price": "1020.00",
                            "price_extra": "0.00",
                            "price_org": "1020.00"
                        },
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20160123T210000Z\r\nDTEND;VALUE=DATE-TIME:20160124T160000Z\r\nEND:VEVENT\r\n",
                            "current": false,
                            "id": "5661d2fc9cb5385800d87210",
                            "price": "1200.00",
                            "price_extra": "0.00",
                            "price_org": "1200.00"
                        }
                    ],
                    "seats": null,
                    "sector": null
                },
                {
                    "amount": 100,
                    "amount_vacant": 92,
                    "id": "5661d3959cb5385800d8749d",
                    "name": "Партер 1-10 ряд (свободная рассадка)",
                    "pos": 0,
                    "price": "1400.00",
                    "price_extra": "0.00",
                    "price_org": "1400.00",
                    "rules": [
                        {
                            "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20151206T210000Z\r\nDTEND;VALUE=DATE-TIME:20160124T160000Z\r\nEND:VEVENT\r\n",
                            "current": true,
                            "id": "566588e79cb53818afee1075",
                            "price": "1400.00",
                            "price_extra": "0.00",
                            "price_org": "1400.00"
                        }
                    ],
                    "seats": null,
                    "sector": null
                }
            ],
            "status": "public",
            "tags": [
                "концерты"
            ],
            "ticket_template": null,
            "tickets_amount": 230,
            "tickets_amount_vacant": 201,
            "title": {
                "desc": "Выдающийся итальянский органист Вальтер Д’Арканджело раскрывает звуковое великолепие органа собора св. Петра в своей новой программе. Он открывает сокровищницу романтической органной музыки и предлагает путешествие по лабиринтам эпохи. Центр программы — шедевры великих французских композиторов-органистов С. Франка, Л. Вьерна, Л. Лефебюра-Вели, Ж. Алена и Л. Боэльмана. «Готическая сюита», «Висячие сады», «Карильон» — уже сами названия рождают фантастические образы, которые с поразительным мастерством воплощены в звуках. Д’Арканджело исполнит не только классику XIX века, но и редкие жемчужины европейского репертуара: пьесы немецких композиторов Ф. Вагнера, О. Динела, и своего соотечественника — итальянца В. Петрали.   \n\nВ программе: С.Франк, Ф. Вагнер, Л. Вьерн, Л. Лефебюр-Вели, В. Петрали, Ж. Ален, Л. Боэльман.",
                "text": "\"Солнечная Италия\" Играет Вальтер Д'Арканжело"
            },
            "updated_at": "2016-01-13T16:52:34.944000+00:00",
            "venue": {
                "address": "Старосадский 7/10",
                "city": {
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
                    "timezone": "Europe/Moscow"
                },
                "country": {
                    "id": "RU",
                    "name": {
                        "be": "Расійская Федэрацыя",
                        "default": "Russia",
                        "en": "Russia",
                        "fr": "Russie",
                        "ru": "Россия",
                        "zh": "俄罗斯"
                    }
                },
                "desc": null,
                "id": "564c68ff9cb5387eedb8a20b",
                "name": "Евангелическо-лютеранский Кафедральный собор свв. Петра и Павла в Москве*",
                "point": {
                    "coordinates": [
                        37.639563599999974,
                        55.7565658
                    ],
                    "type": "Point"
                }
            }
        }
    ]
