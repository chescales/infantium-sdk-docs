.. _get-teacher:

======================================================
GET teacher/ID
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Gets all the information about a *Teacher*.

.. seealso::

    :mod:`Parent` and :mod:`Teacher` Resources
        The *Tutors* in Infantium's Platform.

***************
Resource URL
***************

``https//SERVER/api/v1/teacher``

********************
Parameters
********************

None

********************
Example request
********************

Example of a GET teacher:

**URL:** ``https://SERVER/api/v1/teacher/100/?api_username=USERNAME\&api_key=API_KEY``

**Request body:**

.. code-block:: json

    {
        "completed": true,
        "country_code": "US",
        "id": 149,
        "preferred_language": "en",
        "resource_uri": "/api/v1/parent/149/",
        "sex": "F",
        "show_tips": true,
        "subscribed": false,
        "user": "/api/v1/user/175/",
        "userprofile_uuid": "37f29070fb174d52ac6a4ff6e4b6213e"
    }
