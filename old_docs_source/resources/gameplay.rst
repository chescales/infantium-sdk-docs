========================================================
:mod:`GamePlay` --- Information about a Game
========================================================

.. module:: GamePlay
   :synopsis: Information about a player in a Game.
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

The *GamePlay* resource simulates one game session for a specific *Player*. This game session is related to other
resources like *Player* who is using the App, and the *ContentApp* itself that the player is interacting with. This
*ContentApp* resource includes information like the platform, price, device, and other particular information about
one *Content* deployed in a physical environment.

..  seealso::

    :mod:`Player` Resource
        The final player of the App.

    :ref:`get-gameplay`
        Gets the information about a specific *GamePlay*.

    :ref:`post-gameplay`
        Creates a new *GamePlay*.

***************
Field reference
***************

The resource *GamePlay* contains the following fields:

+-------------------------+-------------+---------------------------------------------------+
| Field                   | Type        | Description                                       |
+=========================+=============+===================================================+
| ``id``                  | Integer     | Unique identifier for the resource                |
+-------------------------+-------------+---------------------------------------------------+
| ``is_playing``          | Boolean     | This value indicates if the GamePlay has finished |
+-------------------------+-------------+---------------------------------------------------+
| ``start_play``          | DateTime    | The game start date and time                      |
+-------------------------+-------------+---------------------------------------------------+
| ``end_play``            | DateTime    | The game end date and time                        |
+-------------------------+-------------+---------------------------------------------------+
| ``player``              | Resource    | A link to the Player's resource                   |
+-------------------------+-------------+---------------------------------------------------+
| ``contentapp``          | Resource    | A link to the Content App's resource              |
+-------------------------+-------------+---------------------------------------------------+
| ``player_uuid``         | UUID        | A unique id in the system for scoring purposes    |
+-------------------------+-------------+---------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself                |
+-------------------------+-------------+---------------------------------------------------+

Example of a *GamePlay*:

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

