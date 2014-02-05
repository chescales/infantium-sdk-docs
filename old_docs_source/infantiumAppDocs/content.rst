======================================================
:mod:`Content` --- Received as Featured Content
======================================================

.. module:: Content
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

A generic content. This is returned when accessing the *Featured Content*.

.. seealso::

    :mod:`MultimediaContent` Resource

    :mod:`EBookContent` Resource

    :mod:`GameContent` Resource


***************
Field reference
***************

The resource *Content* contains the following fields:

+-------------------------+-------------+-------------------------------------------------+
| Field                   | Type        | Description                                     |
+=========================+=============+=================================================+
| ``id``                  | Integer     | Unique identifier for the resource              |
+-------------------------+-------------+-------------------------------------------------+
| ``name``                | String      | Name of the Content                             |
+-------------------------+-------------+-------------------------------------------------+
| ``min_age_months``      | Integer     | Minimum recommended age in months               |
+-------------------------+-------------+-------------------------------------------------+
| ``max_age_months``      | Integer     | Maximum recommended age in months               |
+-------------------------+-------------+-------------------------------------------------+
| ``short_desc``          | String      | Short Content description                       |
+-------------------------+-------------+-------------------------------------------------+
| ``long_desc``           | String      | Full Content description                        |
+-------------------------+-------------+-------------------------------------------------+
| ``main_image``          | URL         | Relative URL to the image                       |
+-------------------------+-------------+-------------------------------------------------+
| ``developer``           | Resource    | A link to the developer resource                |
+-------------------------+-------------+-------------------------------------------------+
| ``languages``           | List        | A list of Languages                             |
+-------------------------+-------------+-------------------------------------------------+
| ``strengths``           | List        | A list of Strings (each strength)               |
+-------------------------+-------------+-------------------------------------------------+
| ``content_uuid``        | UUID        | A unique id in the system for scoring purposes  |
+-------------------------+-------------+-------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself              |
+-------------------------+-------------+-------------------------------------------------+

Example of a *Content*:

.. code-block:: json

    {
        "content_uuid": "dc0cgaj354544ffe94621a56801f5b91",
        "developer": "/api/v1/developer/100/",
        "id": 6,
        "languages": ["/api/v1/languagecontent/2/", "/api/v1/languagecontent/1/"],
        "long_desc": "Chup On has been........ ",
        "main_image": "/media/contents/images/chupon.png",
        "max_age_months": 36,
        "min_age_months": 12,
        "name": "ChupOn",
        "resource_uri": "/api/v1/gamecontent/6/",
        "short_desc": "Chup On has been............",
        "strengths": ["math", "linguistic", "simbolycal"],
    }
