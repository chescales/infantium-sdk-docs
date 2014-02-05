==================
REST API v2
==================

The API in Infantium is presented as a RESTful API, currently in version 2.0. The access methods represented in HTTP
requests are ``POST``, ``GET``, ``PUT`` and ``DELETE``, and are furtherly explained in this section.

.. warning::

    It is mandatory to access the API with a valid **API_USERNAME** and **API_KEY**. Each developer will have its own
    values provided by an Infantium's representative. Check the :ref:`authorization` section for further information.

The different API calls available for developers in Infantium's API are the following:

***************
GamePlay
***************

:ref:`get-gameplay`

:ref:`post-gameplay`

:ref:`post-gameplay-finish`

***************
Parent
***************

:ref:`get-parent`

***************
Player
***************

:ref:`get-player`

:ref:`post-player`

:ref:`put-player`

***************
RawData
***************

:ref:`post-rawdata`

***************
Teacher
***************

:ref:`get-teacher`


.. toctree::
    :maxdepth: 2
    :hidden:

    restapi/get/gameplay.rst
    restapi/post/gameplay.rst
    restapi/post/gameplay/ID/finish.rst
    restapi/get/parent.rst
    restapi/get/player.rst
    restapi/post/player.rst
    restapi/put/player.rst
    restapi/post/rawdata.rst
    restapi/get/teacher.rst
