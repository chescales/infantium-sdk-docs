.. _post-gameplay-finish:

======================================================
POST gameplay/ID/finish
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Finishes the *GamePlay* resource pointed by the required ID parameter. This is intended to indicate the Platform that
no more *RawData* messages about the *GamePlay* will be sent.

.. seealso::

    :mod:`Player` Resource
        The final player of the App.

    :mod:`GamePlay` Resource
        Information about a Game.

    :ref:`post-gameplay`
        Create a new *GamePlay*

    :ref:`post-rawdata`
        Send new *RawData*

***************
Resource URL
***************

``https//SERVER/api/v1/gameplay/ID/finish``

********************
Parameters
********************

None

********************
Example request
********************

Example of a POST gameplay/ID/finish:

**URL:** ``https://SERVER/api/v1/gameplay/300/finish/?api_username=USERNAME\&api_key=API_KEY``

**Body:**

.. code-block:: json

   {
   }
