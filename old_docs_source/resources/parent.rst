========================================================
:mod:`Parent` --- User Specialization
========================================================

.. module:: Parent
   :synopsis: Specific Information about a Parent.
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

The *Parent* resource is an extension of a *User* which is specifically a parent of the child, or said in another way,
is the tutor of a child or a small group of children (not in a class like for the Teacher resource). As such, it has
a particular set of fields detailed below.

The *Parent* will then have the possibility to create one or more players, and start playing the Apps of his/her choice
inside Infantium's Platform.

.. seealso::

   :mod:`Player` Resource
       The final player of the App.

   :mod:`Teacher` Resource
       The other type of *Tutor* in Infantium's Platform.

   :mod:`User` Resource
       General Information about a Tutor.

***************
Field reference
***************

The resource *Parent* contains the following fields:

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

Example of a *Parent*:

.. code-block:: json

    {
        "completed": true,
        "country_code": "US",
        "id": 149,
        "preferred_language": "en",
        "resource_uri": "/api/v1/parent/149/",
        "sex": "F",
        "show_tips": true,
        "subscribed": false,
        "user": "/api/v1/user/175/",
        "userprofile_uuid": "37f29070fb174d52ac6a4ff6e4b6213e"
    }

