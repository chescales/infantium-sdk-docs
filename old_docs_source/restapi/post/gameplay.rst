.. _post-gameplay:

======================================================
POST gameplay
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Creates a new *GamePlay* resource. This is intended to record the information related to one *Player* playing an App
during a certain period of time.

.. seealso::

    :mod:`Player` Resource
        The final player of the App.

    :mod:`GamePlay` Resource
        Information about a Game.

***************
Resource URL
***************

``https//SERVER/api/v1/gameplay/``

********************
Parameters
********************

+---------------------------+---------------------------------------------------------------------------+
| Field                     | Description                                                               |
+===========================+===========================================================================+
| | ``player``              | | A link to the Player's resource.                                        |
| | *(required)*            | | **Example Value:** /api/v1/player/150/                                  |
+---------------------------+---------------------------------------------------------------------------+
| | ``contentapp``          | | A link to the Content App's resource                                    |
| | *(required)*            | | **Example Value:** /api/v1/contentapp/10/                               |
+---------------------------+---------------------------------------------------------------------------+
| | ``is_playing``          | | This boolean value indicates if the GamePlay has finished.              |
| | *(required)*            | | **Example Value:** true                                                 |
+---------------------------+---------------------------------------------------------------------------+

********************
Example request
********************

Example of a POST gameplay:

**URL:** ``https://SERVER/api/v1/gameplay/?api_username=USERNAME\&api_key=API_KEY``

**Body:**

.. code-block:: json

   {
       "contentapp": "/api/v1/contentapp/10/",
       "is_playing": true,
       "player": "/api/v1/player/150/"
   }
