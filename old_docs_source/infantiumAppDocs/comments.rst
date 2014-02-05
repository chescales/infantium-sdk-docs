======================================================
:mod:`Comments and Ratings`
======================================================

.. module:: CommentsRatings
.. moduleauthor:: Chesco Igual <chesco@infantium.com>
.. sectionauthor:: Chesco Igual <chesco@infantium.com>

Comments and ratings associated to a *Content*.

.. seealso::

    :mod:`Content` Resource


***************
Field reference
***************

The resource *Comments and Ratings* contains the following fields:

+-------------------------+-------------+-------------------------------------------------+
| Field                   | Type        | Description                                     |
+=========================+=============+=================================================+
| ``id``                  | Integer     | Unique identifier for the resource              |
+-------------------------+-------------+-------------------------------------------------+
| ``comment``             | String      | Comment written by the user                     |
+-------------------------+-------------+-------------------------------------------------+
| ``rating``              | Integer     | Rating from 1 to 5                              |
+-------------------------+-------------+-------------------------------------------------+
| ``submit_date``         | Datetime    | Date posted                                     |
+-------------------------+-------------+-------------------------------------------------+
| ``user_name``           | String      | Name of the user who posted it                  |
+-------------------------+-------------+-------------------------------------------------+

Example of a *Comment and Rating*:

.. code-block:: json

    {
        "comment": "Please not anymore!",
        "id": 186,
        "rating": 1,
        "submit_date": "2013-03-06T13:25:03.075886",
        "user_name": "Peter Griffin"
    }