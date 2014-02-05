======================================================
:mod:`ContentApp`
======================================================

.. module:: ContentApp
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

A specific App for a platform and device of one *Content*.

.. seealso::

    :mod:`Content` Resource


***************
Field reference
***************

The resource *ContentApp* contains the following fields:

+-------------------------+-------------+-------------------------------------------------+
| Field                   | Type        | Description                                     |
+=========================+=============+=================================================+
| ``id``                  | Integer     | Unique identifier for the resource              |
+-------------------------+-------------+-------------------------------------------------+
| ``content``             | Resource    | Link to the parent Content Resource             |
+-------------------------+-------------+-------------------------------------------------+
| ``version``             | String      | Software version                                |
+-------------------------+-------------+-------------------------------------------------+
| ``platform``            | Choices     | One of [IOS, DROI, WIN8, FIRE]                  |
+-------------------------+-------------+-------------------------------------------------+
| ``country``             | Country     | Two-char coded country                          |
+-------------------------+-------------+-------------------------------------------------+
| ``device``              | Choices     | One of [TAB, TAB7, TAB10, MOB, DESK]            |
+-------------------------+-------------+-------------------------------------------------+
| ``freemium_mode``       | Choices     | One of [FREE, LITE, PREM, FULL]                 |
+-------------------------+-------------+-------------------------------------------------+
| ``downloads``           | Integer     | Number of downloads                             |
+-------------------------+-------------+-------------------------------------------------+
| ``buys``                | Integer     | Number of purchases                             |
+-------------------------+-------------+-------------------------------------------------+
| ``price``               | Float       | Original price                                  |
+-------------------------+-------------+-------------------------------------------------+
| ``discount``            | Float       | Discount over the price                         |
+-------------------------+-------------+-------------------------------------------------+
| ``contentapp_uuid``     | UUID        | A unique id in the system for scoring purposes  |
+-------------------------+-------------+-------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself              |
+-------------------------+-------------+-------------------------------------------------+

Example of a *ContentApp*:

.. code-block:: json

    {
        "buys": 0,
        "contentapp_uuid": "3cea3d36531d48f790b787b013b9a5da",
        "country": "ES",
        "device": "TAB",
        "discount": "0.00",
        "discount_currency": "EUR",
        "downloads": 0,
        "fremium_mode": "LITE",
        "id": 3,
        "language": "en",
        "platform": "IOS",
        "price": "0.00"
        "price_currency": "EUR",
        "resource_uri": "/api/v1/contentapp/3/",
        "version": "2.0"
    }
