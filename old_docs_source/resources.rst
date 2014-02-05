==================
Platform Resources
==================

A core concept in a REST web service like ours is the existence of resources (sources of specific information),
each of which is referenced with a global identifier (a URI in our case). In order to interact with those resources,
users or software agents communicate by using standard HTTP messages, also known as CRUD methods
(create, read, update and delete). Those methods are represented in HTTP requests as ``POST``, ``GET``, ``PUT``
and ``DELETE``.

The different resources available for developers in Infantium's API are the following:

.. toctree::
   :maxdepth: 2

   resources/gameplay.rst
   resources/parent.rst
   resources/player.rst
   resources/rawdata.rst
   resources/teacher.rst
   resources/user.rst