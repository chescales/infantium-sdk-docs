========================================================
:mod:`User` --- General Information
========================================================

.. module:: User
   :synopsis: General Information about a Tutor.
.. moduleauthor:: Dani Gonzalez <danigosa@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

The *User* resource represents the main user management class in our Platform. It contains the authentication
information for the Platform, and it is used to store some core information about every user like its username
and password, or even its e-mail address.

Deeper in the Platform, each user is specialized in one of several types like *Parent* or *Teacher*, with additional
fields, and which will be related to the different *Players* of the Apps. However, the *User* resource remains
responsible for tasks such as ``login``, ``logout`` and ``register``.

.. seealso::

   :mod:`Player` Resource
       The final player of the App.

   :mod:`Parent` and :mod:`Teacher` Resources
       The *Tutors* in Infantium's Platform.

***************
Field reference
***************

The resource *User* contains the following fields:

+-------------------------+-------------+----------------------------------------------------+
| Field                   | Type        | Description                                        |
+=========================+=============+====================================================+
| ``id``                  | Integer     | Unique identifier for the resource                 |
+-------------------------+-------------+----------------------------------------------------+
| ``username``            | String      | Unique username for login purposes                 |
+-------------------------+-------------+----------------------------------------------------+
| ``first_name``          | String      | First name of the user                             |
+-------------------------+-------------+----------------------------------------------------+
| ``last_name``           | String      | Last name of the user                              |
+-------------------------+-------------+----------------------------------------------------+
| ``date_joined``         | DateTime    | The creation date and time of the user             |
+-------------------------+-------------+----------------------------------------------------+
| ``last_login``          | DateTime    | The last login date and time of the user           |
+-------------------------+-------------+----------------------------------------------------+
| ``is_active``           | Boolean     | Boolean indicating if the user is active or banned |
+-------------------------+-------------+----------------------------------------------------+
| ``resource_uri``        | Resource    | A link to the resource item itself                 |
+-------------------------+-------------+----------------------------------------------------+

Example of a *User*:

.. code-block:: json

   {
       "date_joined": "2013-02-13T10:02:02.960398",
       "first_name": "Peter",
       "id": 175,
       "is_active": true,
       "last_login": "2013-02-20T10:41:37.396409",
       "last_name": "Griffin",
       "resource_uri": "/api/v1/user/175/",
       "username": "peter_griffin@parents.com"
   }

