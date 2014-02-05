======================================================
:mod:`Player` --- The final user of the platform
======================================================

.. module:: Player
   :synopsis: Information about the players of the contents.
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Players are the final users of the contents provided by the Infantium Platform. They will usually be the children
that, supervised by a tutor will play the *Games*, read the *EBooks* and view the *Media* in our platform,
and whose *GamePlay* information we will collect in order to provide our service.

Players usually will have an associated *Tutor*, but in the current version of the API it is possible to create one
without associating an existing one. This will cause the system to create an *anonymous Tutor*, which will have the
possibility to register after playing the game.

.. seealso::

    :mod:`GamePlay` Resource
        Information about games played.

    :mod:`Parent` and :mod:`Teacher` Resources
        The *Tutors* in Infantium's Platform.

***************
Field reference
***************

The resource *Player* contains the following fields:

+-------------------------+-------------+-------------------------------------------------+
| Field                   | Type        | Description                                     |
+=========================+=============+=================================================+
| ``id``                  | Integer     | Unique identifier for the resource              |
+-------------------------+-------------+-------------------------------------------------+
| ``nickname``            | String      | Unique string together with tutor               |
+-------------------------+-------------+-------------------------------------------------+
| ``months``              | Integer     | The age of the player in months                 |
+-------------------------+-------------+-------------------------------------------------+
| ``tutor``               | Resource    | A link to the Tutor of the child                |
+-------------------------+-------------+-------------------------------------------------+
| ``sex``                 | Choices     | {'U': undefined, 'B': boy, 'G': girl}           |
+-------------------------+-------------+-------------------------------------------------+
| ``avatar``              | Image       | The player's avatar                             |
+-------------------------+-------------+-------------------------------------------------+
| ``avatar_url``          | String      | A static url to the image in Infantium's server |
+-------------------------+-------------+-------------------------------------------------+
| ``avatar_height_field`` | Integer     | The height of the avatar                        |
+-------------------------+-------------+-------------------------------------------------+
| ``avatar_width_field``  | Integer     | The width of the avatar                         |
+-------------------------+-------------+-------------------------------------------------+
| ``player_uuid``         | UUID        | A unique id in the system for scoring purposes  |
+-------------------------+-------------+-------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself              |
+-------------------------+-------------+-------------------------------------------------+

Example of a *Player*:

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
