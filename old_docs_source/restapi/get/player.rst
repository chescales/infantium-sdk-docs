.. _get-player:

======================================================
GET player/ID
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Gets all the information related to a specific *Player*.

.. seealso::

    :mod:`Player` Resource
        The final player of the App.

    :mod:`Parent` and :mod:`Teacher` Resources
        The *Tutors* in Infantium's Platform.

    :ref:`post-player`
        Create a new *Player*.

    :ref:`put-player`
        Update an existing *Player*.

***************
Resource URL
***************

``https//SERVER/api/v1/player/ID``

********************
Parameters
********************

None

********************
Example request
********************

Example of a GET player:

**URL:** ``https://SERVER/api/v1/player/200/?api_username=USERNAME\&api_key=API_KEY``

**Response body:**

.. code-block:: json

    {
        "avatar": "/media/players/avatar/cfeec5b7-f324-42.png",
        "avatar_height_field": 140,
        "avatar_url": null,
        "avatar_width_field": 140,
        "id": 234,
        "months": 21,
        "nickname": "Stewie",
        "player_uuid": "05e3d6441b8645bc99303da9fc702586",
        "resource_uri": "/api/v1/player/234/",
        "sex": "B",
        "tutor": "/api/v1/tutor/149/"
    }
