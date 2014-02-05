=================================================================
:mod:`GameContent` --- Also received as Personalized Game Content
=================================================================

.. module:: GameContent
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

A content which is specifically a game App.

.. seealso::

    :mod:`Content` Resource

    :mod:`MultimediaContent` Resource

    :mod:`EBookContent` Resource


***************
Field reference
***************

The resource *GameContent* contains the following fields:

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
| ``levels``              | Integer     | The number of levels                            |
+-------------------------+-------------+-------------------------------------------------+
| ``url_scheme``          | URL         | A link to the external content                  |
+-------------------------+-------------+-------------------------------------------------+
| ``content_uuid``        | UUID        | A unique id in the system for scoring purposes  |
+-------------------------+-------------+-------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself              |
+-------------------------+-------------+-------------------------------------------------+

Example of a *GameContent*:

.. code-block:: json

    {
        "content_uuid": "dc0cgaj354544ffe94621a56801f5b91",
        "developer": "/api/v1/developer/100/",
        "id": 6,
        "languages": ["/api/v1/languagecontent/2/", "/api/v1/languagecontent/1/"],
        "levels": 200,
        "long_desc": "Chup On has been........ ",
        "main_image": "/media/contents/images/chupon.png",
        "max_age_months": 36,
        "min_age_months": 12,
        "name": "ChupOn",
        "resource_uri": "/api/v1/gamecontent/6/",
        "short_desc": "Chup On has been............",
        "strengths": ["math", "linguistic", "simbolycal"],
        "url_scheme": "https://itunes.apple.com/us/app/chup-on/id572416590?mt=8&ign-msr=http%3A%2F%2Fwww.chuponapp.com%2F%3Fpage_id%3D58"
    }
