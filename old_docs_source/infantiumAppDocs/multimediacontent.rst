======================================================
:mod:`MultimediaContent`
======================================================

.. module:: MultimediaContent
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

A content which is specifically a multimedia file.

.. seealso::

    :mod:`Content` Resource

    :mod:`GameContent` Resource

    :mod:`EBookContent` Resource


***************
Field reference
***************

The resource *MultimediaContent* contains the following fields:

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
| ``duration``            | Integer     | The duration of the content in seconds          |
+-------------------------+-------------+-------------------------------------------------+
| ``media_url``           | URL         | A link to the downloadable content              |
+-------------------------+-------------+-------------------------------------------------+
| ``content_uuid``        | UUID        | A unique id in the system for scoring purposes  |
+-------------------------+-------------+-------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself              |
+-------------------------+-------------+-------------------------------------------------+

Example of a *MultimediaContent*:

.. code-block:: json

    {
        "content_uuid": "1bc292eb5c5a4d84b8973721326b2983",
        "developer": "/api/v1/developer/100/",
        "duration": 30,
        "id": 3,
        "languages": ["/api/v1/languagecontent/2/", "/api/v1/languagecontent/1/"],
        "long_desc": "Dora the Explorer is an American...... ",
        "main_image": "/media/contents/images/Dora_the_Explorer_logo.svg.png",
        "max_age_months": 24,
        "media_url": "http://en.wikipedia.org/wiki/Dora_the_Explorer",
        "min_age_months": 10,
        "name": "Dora the Explorer",
        "resource_uri": "/api/v1/multimediacontent/3/",
        "short_desc": "Dora the Explorer is an American.....",
        "strengths": ["math", "linguistic", "simbolycal"]
    }
