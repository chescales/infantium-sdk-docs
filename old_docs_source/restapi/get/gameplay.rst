.. _get-gameplay:

======================================================
GET gameplay/ID
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Gets the information about a specific *GamePlay* resource.

.. seealso::

    :mod:`Player` Resource
        The final player of the App.

    :mod:`GamePlay` Resource
        Information about a Game.

    :ref:`post-gameplay`
        Creates a new *GamePlay*.

***************
Resource URL
***************

``https//SERVER/api/v1/gameplay/ID``

********************
Parameters
********************

None

********************
Example request
********************

Example of a GET gameplay:

**URL:** ``https://SERVER/api/v1/gameplay/100/?api_username=USERNAME&api_key=API_KEY``

**Request body:**

.. code-block:: json

    {
        "contentapp": "/api/v1/contentapp/3/",
        "end_play": "2013-02-18T15:57:17.628875",
        "gameplay_uuid": "a22e368b230f4a7297a8329e3f0423fa",
        "id": 289,
        "is_playing": false,
        "player": "/api/v1/player/236/",
        "resource_uri": "/api/v1/gameplay/289/",
        "start_play": "2013-02-18T15:54:01.107683"
    }
