.. _put-player:

======================================================
PUT player/ID
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Updates an existing player.

.. seealso::

    :mod:`Player` Resource
        The final player of the App.

    :mod:`Parent` and :mod:`Teacher` Resources
        The *Tutors* in Infantium's Platform.

    :ref:`get-player`
        Get information about an existing *Player*.

    :ref:`post-player`
        Create a new *Player*.

***************
Resource URL
***************

``https//SERVER/api/v1/player/ID``

********************
Parameters
********************

+---------------------------+---------------------------------------------------------------------------+
| Field                     | Description                                                               |
+===========================+===========================================================================+
| | ``nickname``            | | Player nickname. **Must be unique within each Tutor children**.         |
| | *(optional)*            | | **Example Value:** Stewie                                               |
+---------------------------+---------------------------------------------------------------------------+
| | ``months``              | | The age of the player in months.                                        |
| | *(optional)*            | | **Example Value:** 21                                                   |
+---------------------------+---------------------------------------------------------------------------+
| | ``sex``                 | | Child's gender. {'U': undefined, 'B': boy, 'G': girl}.                  |
| | *(optional)*            | | **Example Value:** B                                                    |
+---------------------------+---------------------------------------------------------------------------+
| | ``tutor``               | | A link to the Tutor resource of the child.                              |
| | *(optional)*            | | **Example Value:** /api/v1/tutor/15/                                    |
+---------------------------+---------------------------------------------------------------------------+

********************
Example request
********************

Example of a PUT player:

**URL:** ``https://SERVER/api/v1/player/200/?api_username=USERNAME\&api_key=API_KEY``

**Body:**

.. code-block:: json

   {
       "months": 21,
       "nickname": "Stewie",
       "sex": "B",
       "tutor": "/api/v1/tutor/15/"
   }
