========================================================
:mod:`Teacher` --- User Specialization
========================================================

.. module:: Teacher
   :synopsis: Specific Information about a Teacher.
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

The *Teacher* resource is an extension of a *User* which is specifically a teacher of a classroom, or said in another way,
is the tutor of a medium-big sized group of children. As such, it has a particular set of fields detailed below.

The *Teacher* will then have the possibility to create several players, and start playing the Apps of his/her choice
inside Infantium's Platform.

.. seealso::

   :mod:`Player` Resource
       The final player of the App.

   :mod:`Parent` Resource
       The other type of *Tutor* in Infantium's Platform.

   :mod:`User` Resource
       General Information about a Tutor.

***************
Field reference
***************

The resource *Teacher* contains the following fields:

+-------------------------+-------------+-----------------------------------------------------------+
| Field                   | Type        | Description                                               |
+=========================+=============+===========================================================+
| ``id``                  | Integer     | Unique identifier for the resource                        |
+-------------------------+-------------+-----------------------------------------------------------+
| ``country_code``        | String      | A two-character code of the country                       |
+-------------------------+-------------+-----------------------------------------------------------+
| ``sex``                 | Choice      | {'U': undefined, 'M': male, 'F': female}                  |
+-------------------------+-------------+-----------------------------------------------------------+
| ``preferred_language``  | String      | A two-character code of the language                      |
+-------------------------+-------------+-----------------------------------------------------------+
| ``user``                | Resource    | A link to the User information of the Parent              |
+-------------------------+-------------+-----------------------------------------------------------+
| ``complete``            | Boolean     | Indicates if the user completed the registration          |
+-------------------------+-------------+-----------------------------------------------------------+
| ``show_tips``           | Boolean     | Boolean indicating if tips should be showed               |
+-------------------------+-------------+-----------------------------------------------------------+
| ``subscribed``          | Boolean     | Indicates if the user is subscribed to mail information   |
+-------------------------+-------------+-----------------------------------------------------------+
| ``userprofile_uuid``    | UUID        | A unique id in the system for scoring purposes            |
+-------------------------+-------------+-----------------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself                        |
+-------------------------+-------------+-----------------------------------------------------------+

Example of a *Teacher*:

.. code-block:: json

   {
       "completed": false,
       "country_code": "US",
       "id": 154,
       "preferred_language": "en",
       "resource_uri": "/api/v1/teacher/154/",
       "sex": "U",
       "show_tips": true,
       "subscribed": true,
       "user": "/api/v1/user/180/",
       "userprofile_uuid": "171952cf4a3b46bf838056dfe5b7b791"
   }

