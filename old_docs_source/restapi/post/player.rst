.. _post-player:

======================================================
POST player
======================================================

.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Creates a new player, either with or without a *Tutor*. Players are the final users of the Apps in the Infantium
Platform, namely the children. Each one of the different children playing from the same device should have a different
player, so the Platform can properly calculate their statistics.

.. warning::

   Creating a *Player* without an assigned *Tutor* is a tool provided for final users to play without registration.
   Nevertheless, take into account that a *Parent* account is created in the background, and **following new players**
   **should include the newly created Tutor in their POST parameters**. Any other behavior will create incoherent
   information in the Platform and the final users won't be able to make full use of Infantium's services.

.. seealso::

    :mod:`Player` Resource
        The final player of the App.

    :mod:`Parent` and :mod:`Teacher` Resources
        The *Tutors* in Infantium's Platform.

    :ref:`get-player`
        Get information about an existing *Player*.

    :ref:`put-player`
        Update an existing *Player*.

***************
Resource URL
***************

``https//SERVER/api/v1/player``

********************
Parameters
********************

+---------------------------+---------------------------------------------------------------------------+
| Field                     | Description                                                               |
+===========================+===========================================================================+
| | ``nickname``            | | Player nickname. **Must be unique within each Tutor children**.         |
| | *(required)*            | | **Example Value:** Stewie                                               |
+---------------------------+---------------------------------------------------------------------------+
| | ``months``              | | The age of the player in months.                                        |
| | *(required)*            | | **Example Value:** 21                                                   |
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

Example of a POST player:

**URL:** ``https://SERVER/api/v1/player/?api_username=USERNAME\&api_key=API_KEY``

**Body:**

.. code-block:: json

   {
       "months": 21,
       "nickname": "Stewie",
       "sex": "B",
       "tutor": "/api/v1/tutor/15/"
   }
