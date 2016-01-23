.. _simple/ps:

=================
Платёжные системы
=================

.. _simple/ps/api:

api/BASE
========

:term:`Платёжная система` `api/BASE` используется для проведения заказа по api.
В этом случае деньги за заказ каким-либо образом берёт сам продавец.

.. EXAMPLE
.. Простой пример попупки через API.


.. _simple/ps/platron:

Platron
=======

Если вы хотите, чтобы покупатели оплачивал заказ через платрон, нужно выбрать
платёжную систему из :ref:`списка ниже <simple/ps/platron/list>`.

Алгоритм использования платрона такой:

    * :ref:`создать заказ <simple/orders/create>` и :ref:`добавить билеты <simple/orders/reserve>`;
    * :ref:`установить платёжную систему <simple/orders/ps>` из :ref:`списка ниже <simple/ps/platron/list>`;
    * установить поля ``payment.success_url`` и ``payment.failure_url``;
    * :ref:`перевести заказ <simple/orders/change_status>` в :ref:`in_progress`;
    * перенаправить пользователя на ``payment.redirect_url``;

После чего покупатель оплачивает заказ на сайте платрона и перенаправляется
на ``success_url`` или ``failure_url``, а заказ переходит в
:ref:`done` (в случае успеха), :ref:`canceled` (в случае отмены) или :ref:`expired` (в случае неоплаты).

.. EXAMPLE
.. Простой пример попупки через платрон.

.. _simple/ps/platron/list:

Список платёжных систем платрона
--------------------------------

:platron/OTHER: универсальная, способ оплаты покупатель выбирает на сайте платрона;
:platron/RUSSIANSTANDARD: банковские карты;
:platron/CASH: наличные ("евросеть", "связной"...);
:platron/YANDEXMONEY: яндекс деньги;
:platron/ALFACLICK: альфа-клик;
:platron/TEST: тестовая, доступна только на https://stage.ticketscloud.org
    для проверки полного цикла оплаты;
