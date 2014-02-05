======================================================
:mod:`RawData` --- The information handler
======================================================

.. module:: RawData
   :synopsis: Information about how the child is playing.
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

*RawData* is the main tool for Infantium to capture the information about game playing, and thus making all the necessary
analysis about how the player behaves. This data is gathered by the developers of the games, with the guidance of
Infantium, and then sent to Infantium's servers for further processing and analysis.

Each *RawData* content will be different for every game, given it is not the same for a child to play a figures game, than
a colors game, or a sounds game. Each one of them will have different variables and attributes to be captured, so the
specific content that you as a developer have to captured will be personalized to your game.

Anyway, some contents of the *RawData* resource will be common to all developers, as a *RawData* is connected to a
*GamePlay* and a *Player*. Those common parameters are explained below.

.. seealso::

    :mod:`GamePlay` Resource
        Information about games played.

    :mod:`Player` Resource
        The final player of the App.

***************
Field reference
***************

The resource *RawData* contains the following fields:

+-------------------------+-------------+-------------------------------------------------+
| Field                   | Type        | Description                                     |
+=========================+=============+=================================================+
| ``id``                  | Integer     | Unique identifier for the resource              |
+-------------------------+-------------+-------------------------------------------------+
| ``contentapp_uuid``     | UUID        | The content app's unique ID                     |
+-------------------------+-------------+-------------------------------------------------+
| ``gameplay_uuid``       | UUID        | The game play's unique ID                       |
+-------------------------+-------------+-------------------------------------------------+
| ``player_uuid``         | UUID        | The game player's unique ID                     |
+-------------------------+-------------+-------------------------------------------------+
| ``data``                | JSON        | Data file in JSON codification about the game   |
+-------------------------+-------------+-------------------------------------------------+
| ``rawdata_uuid``        | UUID        | A unique id in the system for scoring purposes  |
+-------------------------+-------------+-------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself              |
+-------------------------+-------------+-------------------------------------------------+

Example of a *RawData*:

.. code-block:: json

   {
       "contentapp_uuid": "51247e44da82833a5a859aabf235d202",
       "data": "{'responsiveness': {'time_to_respond': 1000}, ............",
       "gameplay_uuid": "4da82833a5a84810a1fd8703db57f435",
       "id": 23,
       "player_uuid": "a96dbffdc6c34e59aabf2d3c75364438",
       "rawdata_uuid": "8ad30294fa574bb6816062e4b2209a3b",
       "resource_uri": "/api/v1/rawdata/23/",
   }
