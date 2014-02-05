.. _post-rawdata:

======================================================
POST rawdata
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Contains the core information about how a *Player* is playing an App. The contents in the *data* field will be
specific for each App. If you still do not have yours, please contact an Infantium's representative.

.. seealso::

    :mod:`Player` Resource
        The final player of the App.

    :mod:`RawData` Resource
        The information handler.

***************
Resource URL
***************

``https//SERVER/api/v1/rawdata``

********************
Parameters
********************

+---------------------------+---------------------------------------------------------------------------+
| Field                     | Description                                                               |
+===========================+===========================================================================+
| | ``contentapp_uuid``     | | The content app's unique ID.                                            |
| | *(required)*            | | **Example Value:** 51247e44da82833a5a859aabf235d202                     |
+---------------------------+---------------------------------------------------------------------------+
| | ``gameplay_uuid``       | | The game play's unique ID.                                              |
| | *(required)*            | | **Example Value:** 4da82833a5a84810a1fd8703db57f435                     |
+---------------------------+---------------------------------------------------------------------------+
| | ``player_uuid``         | | The game player's unique ID.                                            |
| | *(required)*            | | **Example Value:** a96dbffdc6c34e59aabf2d3c75364438                     |
+---------------------------+---------------------------------------------------------------------------+
| | ``data``                | | Data file in JSON codification about the game.                          |
| | *(required)*            | |                                                                         |
+---------------------------+---------------------------------------------------------------------------+

********************
Example request
********************

Example of a POST rawdata:

**URL:** ``https://SERVER/api/v1/rawdata/?api_username=USERNAME\&api_key=API_KEY``

**Body:**

.. code-block:: json

   {
       "contentapp_uuid": "51247e44da82833a5a859aabf235d202",
       "data": "{'responsiveness': {'time_to_respond': 1000}, ............",
       "gameplay_uuid": "4da82833a5a84810a1fd8703db57f435",
       "player_uuid": "a96dbffdc6c34e59aabf2d3c75364438",
   }
