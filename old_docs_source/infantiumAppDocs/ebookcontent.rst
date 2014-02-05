======================================================
:mod:`EBookContent`
======================================================

.. module:: EBookContent
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

A content which is specifically an E-Book.

.. seealso::

    :mod:`Content` Resource

    :mod:`MultimediaContent` Resource

    :mod:`GameContent` Resource


***************
Field reference
***************

The resource *EBookContent* contains the following fields:

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
| ``scenes``              | Integer     | The number of levels                            |
+-------------------------+-------------+-------------------------------------------------+
| ``url_scheme``          | URL         | A link to the external content                  |
+-------------------------+-------------+-------------------------------------------------+
| ``autoplay``            | Boolean     | Indicates if the ebook is autoplayed            |
+-------------------------+-------------+-------------------------------------------------+
| ``read_myself``         | Boolean     | Possibility for the kid to read him/herself     |
+-------------------------+-------------+-------------------------------------------------+
| ``read_to_me``          | Boolean     | Ebook with recorded content                     |
+-------------------------+-------------+-------------------------------------------------+
| ``media_url``           | URL         | A link to the downloadable content              |
+-------------------------+-------------+-------------------------------------------------+
| ``content_uuid``        | UUID        | A unique id in the system for scoring purposes  |
+-------------------------+-------------+-------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself              |
+-------------------------+-------------+-------------------------------------------------+

Example of a *EBookContent*:

.. code-block:: json

    {
        "autoplay": false,
        "content_uuid": "bbfe59ad1ba64d6bba7a43fa63a4ce0a",
        "developer": "/api/v1/developer/100/",
        "id": 4,
        "languages": ["/api/v1/languagecontent/2/", "/api/v1/languagecontent/1/"],
        "long_desc": "The series follows the exploits of a village of indomitable Gauls....",
        "main_image": "/media/contents/images/300px-Asterix_-_Cast.png",
        "max_age_months": 36,
        "media_url": "http://en.wikipedia.org/wiki/Asterix",
        "min_age_months": 30,
        "name": "The Adventures of Asterix",
        "read_myself": true,
        "read_to_me": false,
        "resource_uri": "/api/v1/ebookcontent/4/",
        "scenes": 34,
        "short_desc": "Asterix or The Adventures of Asterix ....",
        "strengths": ["math", "linguistic", "simbolycal"],
        "url_scheme": "http://en.wikipedia.org/wiki/Asterix"
    }
