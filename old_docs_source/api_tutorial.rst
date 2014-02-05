.. Infantium documentation master file, created by
   sphinx-quickstart on Wed Nov 28 12:47:44 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

API Tutorial
=====================================


*********************************************
Getting started
*********************************************

Welcome to Infantium's API tutorial! Following are the first steps for introducing your App to Infantium,
and hopefully create a beautiful long-lasting relationship.

Requirements for the following tutorial::

    HTTP Client
    JSON Encoder/Decoder

.. Comment
    tip:: And by the way...

You will have personalized credentials and database area for your tests.
This information will be provided by Infantium. If you still don't know how to get it, please
send a mail to `developers@infantium.com <developers@infantium.com>`_. The information you will receive is:

* **USERNAME**: Your personal and private username for accessing the application.
* **API_KEY**: The authentication is developed throughout a username + api_key combination on the API url. This key is also personal and non-transferable.
* **CONTENTAPP**: The model of your App on our database. It has several fields as id, uuid, etc.
* **SERVER**: The address of the Infantium servers where to direct the requests.

You can test the API and follow the tutorial using `cUrl <http://http://curl.haxx.se/>`_.

.. _authorization:

*********************************************
Authorization
*********************************************


You must pass your :file:`api_username` and :file:`api_key` in every API call.

.. note:: Every call is stateless, and thus there is no state implemented on the server side.

Your authentication parameters may be passed both by GET or POST:

.. code-block:: http

    https://SERVER/api/v1/RESOURCE_URI/?api_username=API_USERNAME&api_key=API_KEY

From now on in this tutorial we will user dummy values for api_username and api_key.
Use the user and key given by Infantium Team instead of API_USERNAME and API_KEY.


*********************************************
Interacting with the API
*********************************************


Infantium Resources
----------------------------------------------------------------

Resources are the documents with information that the Rest API provides to developers. The resources list is:

* **User**: Login methods are supplied for this resource, as well as some basic user information.
* **Parent**: Additional data about a User who is specifically a Parent. The **userprofile_uuid** and **id** valuesis found in this resource, which will be used all along the tutorial.
* **Teacher**: Additional data about a User who is specifically a Teacher. Same information about **userprofile_uuid**and **id** apply here.
* **Player**: CRUD for Player, the child who actually plays.
* **Content**: CRUD for Content, a grouping resource with information about all contents in the platform.
* **GameContent**: CRUD for GameContent, a specialization of Content.
* **EbookContent**: CRUD for EBookContent, a specialization of Content.
* **MultimediaContent**: CRUD for MultimediaContent, a specialization of Content.
* **ContentApp**: CRUD for ContentApp, which is an App where the content is deployed in a device using a specific OS.
* **GamePlay**: CRUD for GamePlay, the game play entity with game play information.
* **RawData**: CRUD for RawData, with all the tracking done for a GamePlay while the children are playing.

Getting a Resource
----------------------------------------------------------------

Use an HTTP GET request to access resources by URI:

.. code-block:: bash

    $ curl --dump-header - \
    "https://SERVER/api/v1/RESOURCE_URI/?api_username=API_USERNAME&api_key=API_KEY"

Resources are returned using pagination. The API returns two objects, a *meta* field with general information
about the current response, and an *objects* field, which contains a list of dictionaries with the data::

    {
        "meta": {
            "limit": 20,
            "next": null,
            "offset": 0,
            "previous": null,
            "total_count": 0
        },
        "objects": [
            {}
        ]
    }

The parameters returned are:

* **limit**: maximum number of items returned
* **next**: URI for next pagination (will be null if this is the last page)
* **offset**: items offset
* **previous**: URI for previous pagination (will be null if this is the first page)
* **total_count**: total items in list

Giving the GET parameter *limit=0* will avoid pagination and return full list of objects, although it is not recommended.


Posting on the Resources
----------------------------------------------------------------

In order to send information to the API, you should make an HTTP POST request, or in most advanced
cases, an HTTP PUT request (but that is not covered in this tutorial).

.. code-block:: bash

    $ curl --dump-header - -H "Content-Type: application/json" -X POST \
    --data "{'data':'Hello World'}" \
    "https://SERVER/api/v1/RESOURCE_URI/?api_username=API_USERNAME&api_key=API_KEY"

Other Operations
----------------------------------------------------------------

In this tutorial only the very basics of the interaction with the API will be covered. In the full documentation
all the HTTP methods will be covered, but for now only GET and POST should be used.


Supported Formats
----------------------------------------------------------------

The data formats available in the API are:

* **API input**: *JSON* is mandatory (other formats have not been tested, unreliable results may happen)
* **API output**: *JSON*  (XML may be activated if needed)

JSON is the default (and recommended) format for interacting with the API.


Interacting with the Resources
----------------------------------------------------------------

Following are the interactions with the API in order to complete a basic player gameplay. This basic tutorial
will show you the necessary steps to connect your App with our platform, and will point you to more advanced
topics whenever it looks right. The process flow followed will be:

#. Creating an anonymous *Player* (anonymous because it has no registered *Parent* or *Teacher*).
#. Creating a new *GamePlay* for your App.
#. Finishing the current *GamePlay* after the child has finished.
#. Send a RawData resource with the information taken by the App.


.. Users Resource
   *********************************************
.. Login
    ----------------------------------------------------------------
   Login a User to Infantium Platform must be done by a POST call passing :file:`username` and :file:`password`
    as JSON data::
        $ curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"username": "testplayer@infantium.com",\
         "password":"test_player_1234"}' "https://SERVER/api/v1/user/login/?api_username=API_USERNAME&api_key=API_KEY"
    Logout
    ----------------------------------------------------------------
    To logout a user you'll have to be able to store cookies.
    If no session support in client side the session will expire in some time (few time, hours)::
        $ curl --header "SERVER/api/v1/user/logout/?api_username=API_USERNAME&api_key=API_KEY"


*********************************************
Step 1: Player Resource
*********************************************

A player can be created being associated to a *Tutor* (either a *Parent* or a *Teacher*),
or without any *Tutor* predefined (and thus allowing users to play without being registered first).
In order to create players you will have to call our *Player* resource::

    TYPE: GET, POST, PUT
    URI: /api/v1/player/
    GET Parameters: None
    POST Parameters (subset for briefing purposes):
        * nickname: Stewie
        * months: 24
    PUT Parameters: a subset of at least one of POST parameters
        # Important to send the PUT request not to the root uri, but to the URI/ID/

Player Resource Examples
---------------------------------------------------------------

Getting all records using HTTP GET:

.. code-block:: bash

    $ curl --dump-header - \
    https://SERVER/api/v1/player/?api_username=USERNAME\&api_key=API_KEY

Getting a specific record with *id* = *PLAYER_ID* using HTTP GET:

.. code-block:: bash

    $ curl --dump-header - \
    https://SERVER/api/v1/player/PLAYER_ID/?api_username=USERNAME\&api_key=API_KEY

Creating a new *Player* (without *Tutor*) using HTTP POST:

.. code-block:: bash

    $ curl --dump-header - -H "Content-Type: application/json" -X POST \
    --data '{"nickname": "Hannah Montana", "months":"180"}' \
    https://SERVER/api/v1/player/?api_username=USERNAME\&api_key=API_KEY

.. note::

   An HTTP POST request which is successful will return a *LOCATION* header
   with the address to the new resource (together with its id). **This data should be stored for the next step.**

Updating an existing *Player* with *id* = *PLAYER_ID* by using HTTP PUT:

.. code-block:: bash

    $ curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"months":"181"}' \
    https://SERVER/api/v1/player/PLAYER_ID/?api_username=USERNAME\&api_key=API_KEY

.. warning::

   An HTTP PUT message should always be directed to a specific resource item, pointed by *PLAYER_ID*.
   Calling HTTP PUT over the entire collection (i.e. not providing *PLAYER_ID*) will result in an error.

Possible Responses
---------------------------------------------------------------

The possible HTTP responses from the API are:

* HttpResponseOk (200): The GET message has returned some information in the body
* HttpCreated (201): The POST message was successful
* HttpNoContent (204): The PUT message was successful
* HttpUnauthorized (401): Most probably there was a problem with the authentication of your USERNAME and API_KEY.
* HttpForbidden (403): Most likely wrote a wrong URL
* HttpNotFound (404): Same as before. Sometimes even a 200 OK code could be given with wrong information. It is very important that you check the URLs are exactly the same than in the examples.

.. note::

   The most important request in this step is the HTTP POST one, which the App will use to create the player that
   will be playing all along the tutorial.



.. Content Resource
    *********************************************
    What is a content?
    ----------------------------------------------------------------
    Contents supported by Infantium Platform are:
    * **Games**: Games, that's it.
    * **eBooks**: Interactive books. Can be on the form of eBook formats(ePub, etc.), or "game as a book". Autoplay, Read to me and other specific data for a book is supplied.
    * **Multimedia**: Videos and music can also be added as content. If media is not interactive (and usually it's not) it won't use the API.
    Fetching Game and ContentApp Data
    ----------------------------------------------------------------
    Content cannot be modified. Only Contents that developer user is the owner can be listed and fetch, but not modified.
    The main property for the Game is the uuid, which will be useful for creating and fetching other Resources::
        $ curl --dump-header - "https://SERVER/api/v1/content/?api_username=XXXX&api_key=API_KEY"
    The Workflow: Send Data to the Platform
    *********************************************
    To send raw data(the most important and basic operation an integrated app should do) to the platform let's follow these steps.
    1. **Get User Profile (via Login)** / **Get User Profile (Anonimously)**
    2. **Get/Create a Player**
    3. **Create GamePlay**
    4. **Create ScreenPlay**
    5. **Send Rawdata**
    Step One: Get the User Profile
    ----------------------------------------------------------------
    There are two ways to get a valid userprofile object to start creating data for the game. One is using login method and the other is to create anonymously the profile by **not passing any userprofile** in game
    **Create Player via Login**
    This method will require user to give credentials in order to move further the next steps.
    Log user testplayer@infantium.com to get its Profile::
        $ curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"username": "testplayer@infantium.com", "password":"test_player_1234"}' "https://SERVER/api/v1/user/login/?api_username=API_USERNAME&api_key=API_KEY"
    If result is *{"success":"True"}* user will be authenticated.
    In fact, what we really need is the UserProfile resource associated to User. Let's get the profile with this filter call::
        $ curl --dump-header - "https://SERVER/api/v1/userprofile/?api_username=API_USERNAME&api_key=API_KEY&user__username=API_USERNAME
    The result will be something like::
        HTTP/1.1 200 OK
        Server: nginx/1.2.2
        Date: Wed, 28 Nov 2012 19:56:06 GMT
        Content-Type: application/json; charset=utf-8
        Transfer-Encoding: chunked
        Connection: keep-alive
        Vary: Accept-Language, Cookie
        X-Frame-Options: SAMEORIGIN
        Content-Language: en
        Set-Cookie: sessionid=81f7a163f75db85cc6e4f2248f242b3c; expires=Wed, 12-Dec-2012 19:56:06 GMT; httponly; Max-Age=1209600; Path=/; secure
        Set-Cookie: django_language=en; Path=/
        {"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1}, "objects": [{"completed": false, "country_code": "", "id": "3", "image": null, "meta": "{u'empty': u'true'}", "resource_uri": "/api/v1/userprofile/3/", "sex": "", "user": "/api/v1/user/5/"}]}
    We have that user *testplayer@infantium.com* have the uri */api/v1/userprofile/3/*.
    **Create Player Anonymously**
    This method is more flexible but more unsecured (it has several caveats when user uninstall the app or play other games in other devices).
    For obtaining a userprofile that way the only requirement is to create a Player **without** passing the :file:`user_profile` paramenter.
    The platform will create an special user under the hood and will return the userprofile entity bound to the Player. See section create a Player without profile create_player_without_profile_.
    Step Two: Get/Create a Player
    ----------------------------------------------------------------
    Now we can get with the UserProfile the Players associated like this::
        $ curl --dump-header - "https://SERVER/api/v1/player/?api_username=API_USERNAME&api_key=API_KEY&user_profile=3"
    In this case the result is empty::
        $ {"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 0}, "objects": []}
    Let's create a Player with the UserProfile we have::
        $ curl --dump-header - -H "Content-Type: application/json" -X POST \
            --data '{"nickname": "Mariano","months": "18","user_profile": "/api/v1/userprofile/1/","preferred_language" : "es"}'\
            "https://SERVER/api/v1/player/?api_username=API_USERNAME&api_key=API_KEY"
    With this HTTP 201 CREATED response::
        $ HTTP/1.1 201 CREATED
          Server: nginx/1.2.2
          Date: Wed, 28 Nov 2012 20:02:52 GMT
          Content-Type: text/html; charset=utf-8
          Transfer-Encoding: chunked
          Connection: keep-alive
          Vary: Accept-Language, Cookie
          X-Frame-Options: SAMEORIGIN
          Location: https://SERVER/api/v1/player/3/
          Content-Language: en
          Set-Cookie: sessionid=bbbebd81c2edd3999da1be68d10dde51; expires=Wed, 12-Dec-2012 20:02:52 GMT; httponly; Max-Age=1209600; Path=/; secure
          Set-Cookie: django_language=en; Path=/
    Note that the new Player uri is returned in the response, in header **Location: https://SERVER/api/v1/player/3/**.
    Let's take **player_uuid** field for later operations::
        $ curl --dump-header - "https://SERVER/api/v1/player/3/?api_username=API_USERNAME&api_key=API_KEY"
        $ curl --dump-header - "https://SERVER/api/v1/player/3/?api_username=API_USERNAME&api_key=API_KEY"
          HTTP/1.1 200 OK
          Server: nginx/1.2.5
          Date: Tue, 04 Dec 2012 16:30:52 GMT
          Content-Type: application/json; charset=utf-8
          Transfer-Encoding: chunked
          Connection: keep-alive
          Vary: Accept-Language, Cookie
          X-Frame-Options: SAMEORIGIN
          Content-Language: en
          Set-Cookie: sessionid=96d15ca132fe989151e230c2fd24d866; expires=Tue, 18-Dec-2012 16:30:52 GMT; httponly; Max-Age=1209600; Path=/; secure
          Set-Cookie: django_language=en; Path=/
          {"id": "3", "meta": "{u'empty': u'true'}", "months": 18, "nickname": "Mariano", "player_uuid": "PPPP", "preferred_language": "es", "resource_uri": "/api/v1/player/3/", "user_profile": {"completed": false, "country_code": "es", "id": "1", "image": "/static/media/users/avatars/painting.png", "meta": "{}", "resource_uri": "/api/v1/userprofile/1/", "sex": "m", "user": "/api/v1/user/3/"}}
    .. _create_player_without_profile:
    **Create Player Without Profile**
    For anonymous creation of the associated player's profile let's only create a Player without passing :file:`user_profile` JSON parameter::
        curl --dump-header - -H "Content-Type: application/json" -X POST \
                --data '{"nickname": "Mariano","months": "18","preferred_language" : "es"}'\
                "https://SERVER/api/v1/player/?api_username=API_USERNAME&api_key=API_KEY"
    In the response we will have the object uri in Location header. Let's GET the object (via the returned URI) to obtain the needed **userprofile_uuid**.
    .. highlight:: The **userprofile_uuid** is the parameter we must provide when accessing reporting URL. See more about the reporting workflow `here <../getting_started.html#screen-3-main-screen>`_.

*********************************************
Step 2: GamePlay Resource
*********************************************

We have created a player now, so... let's make it play. The next step is create a resource called *GamePlay*
 which simulates a game session of one player. For this request the necessary information will be
 the CONTENTAPP information provided to you about your App, and the player information returned by the
 LOCATION header when we created the player::

    TYPE: GET, POST
    URI: /api/v1/gameplay/
    GET Parameters: None
    POST Parameters:
        * contentapp (required): /api/v1/contentapp/APP_ID/
        * player (required): /api/v1/player/PLAYER_ID/
        * is_playing (required): true

GamePlay Resource Examples
---------------------------------------------------------------

Creating a new *GamePlay* related to a *Player* with *id* = *PLAYER_ID* and your *ContentApp*:

.. code-block:: bash

    $ curl --dump-header - -H "Content-Type: application/json" -X POST \
    --data '{"player": "/api/v1/player/PLAYER_ID/", "contentapp":"/api/v1/contentapp/APP_ID/",\
    "is_playing":"true"}' \
    https://SERVER/api/v1/gameplay/?api_username=USERNAME\&api_key=API_KEY

Possible Responses
---------------------------------------------------------------

The possible HTTP responses from the API are:

* HttpResponseOk (200): The GET message has returned some information in the body
* HttpCreated (201): The POST message was successful
* HttpUnauthorized (401): Most probably there was a problem with the authentication of your USERNAME and API_KEY.
* HttpForbidden (403): Most likely wrote a wrong URL
* HttpNotFound (404): Same as before. Sometimes even a 200 OK code could be given with wrong information. It is very important that you check the URLs are exactly the same than in the examples.



.. Step Three: Create a GamePlay
    ----------------------------------------------------------------
    Given the Game and having created the Player we're able to create one GamePlay (with the URI Location received in previous step)::
        $ curl --dump-header - -H "Content-Type: application/json" -X POST \
            --data '{"is_playing":"1","player":"/api/v1/player/3/","game":"/api/v1/game/2/"}' \
             "https://SERVER/api/v1/gameplay/?api_username=API_USERNAME&api_key=API_KEY"
    This will result in::
        $HTTP/1.1 201 CREATED
         Server: nginx/1.2.2
         Date: Wed, 28 Nov 2012 20:43:41 GMT
         Content-Type: text/html; charset=utf-8
         Transfer-Encoding: chunked
         Connection: keep-alive
         Vary: Accept-Language, Cookie
         X-Frame-Options: SAMEORIGIN
         Location: https://SERVER/api/v1/gameplay/2/
         Content-Language: en
         Set-Cookie: sessionid=731c4e4470d372904c0c0a39959fa795; expires=Wed, 12-Dec-2012 20:43:41 GMT; httponly; Max-Age=1209600; Path=/; secure
         Set-Cookie: django_language=en; Path=/
    Having in response header **Location** the created resource uri.
    If we GET the resource we will have all the info necessary::
        $ curl --dump-header - "https://SERVER/api/v1/gameplay/2/?api_username=API_USERNAME&api_key=API_KEY"
        $ {"end_play": null, "game": {"game_uuid": "ZZZZ", "id": "2", "long_desc": \
            "Rufi and the Magic Paintings", "max_age_months": 40, "meta": "{u'empty': u'true'}", \
            "min_age_months": 18, "name": "Rufi and The Magic Paintings", "resource_uri": "/api/v1/game/2/",\
            "short_desc": "Rufi and the Magic Paintings"}, "gameplay_uuid": "GGGG",\
            "gameroute_set": [], "id": "2", "is_playing": true, "meta": "{u'empty': u'true'}",\
            "player": {"id": "3", "meta": "{u'empty': u'true'}", \
            "months": 18, "nickname": "Mariano", "player_uuid": "PPPP", \
            "preferred_language": "es", "resource_uri": "/api/v1/player/3/", \
            "user_profile": {"completed": false, "country_code": "es", "id": "1", \
            "image": "/static/media/users/avatars/painting.png", "meta": "{}", "resource_uri": "/api/v1/userprofile/1/", \
            "sex": "m", "user": "/api/v1/user/3/"}}, "resource_uri": "/api/v1/gameplay/2/", "start_play": "2012-12-04T16:41:18.970045+00:00"}
    In this result we have to gather the following uuids: **game_uuid, gameplay_uuid and gameroute_uuid**.
.. Step Four: Create the ScreenPlay
    ----------------------------------------------------------------
    ScreenPlay object gives information about the current screen player is playing. It has two important parameters: :file:`order` and
    :file:`level`:
    * **order**: The order the screen's been played. It's the natural order of creation in almost all cases.
    * **level**: The current level the screen belongs to. Every Game has a :file:`levels` attribute. Current level represents
     the actual progress for the whole game.
    In order to create a ScreenPlay we have to call this method::
         curl --dump-header - -H "Content-Type: application/json" -X POST \
         --data '{"gameroute":"/api/v1/gameroute/1/", "order":1, "level":1}' \
         "http://localhost:8000/api/v1/screenplay/?api_username=API_USERNAME&api_key=API_KEY&game_uuid=ZZZZ"
    The result returned will give you the necessary :file:`screenplay_uuid` field used in the final step 5::
        {"gameroute": "/api/v1/gameroute/1/", "id": "4", "level": 1, "meta": "{u'empty': u'true'}", "order": 1, \
        "resource_uri": "/api/v1/screenplay/4/", "screenplay_uuid": "TTTT"}

*********************************************
Step 3: RawData Resource
*********************************************

The next step before the child finishes playing is to send the information related to how the
child is playing the game. In order to do that in a simple way, we will forget about what contents should or should
not be sent, because this step will involve sending kind of complex data structures that are of no use at this step of
the process. In order to simplify this, you can download :download:`this JSON file <_static/json/rawdata.1.0.json>`
with the information related to this last step. We will send that .json information over to the server, and a RawData
resource will be created with fictional (but good enough to be real) information::

    TYPE: POST
    URI: /api/v1/rawdata/
    POST Parameters:
        * Too many at this point. Instead: rawdata.1.0.json file.

RawData Resource Examples
---------------------------------------------------------------

Creating a new *RawData* related to a *GamePlay*, a *Player* and a *ContentApp*:

.. code-block:: bash

    $ curl --dump-header - -H "Content-Type: application/json" -X POST \
    --data @rawdata.1.0.json \
    https://SERVER/api/v1/rawdata/?api_username=USERNAME\&api_key=API_KEY

Possible Responses
---------------------------------------------------------------

The possible HTTP responses from the API are:

* HttpCreated (201): The POST message was successful
* HttpUnauthorized (401): Most probably there was a problem with the authentication of your USERNAME and API_KEY.
* HttpForbidden (403): Most likely wrote a wrong URL
* HttpNotFound (404): Same as before. Sometimes even a 200 OK code could be given with wrong information. It is very important that you check the URLs are exactly the same than in the examples.


*********************************************
Step 4: GamePlay Finishing
*********************************************

And finally, the last step. The game has finished, no more data is going to be sent, and we want to notify Infantium's
Platform about that. In order to finish the *GamePlay*, we will need to contact again with the *GamePlay* resource,
more specifically with the one we created in step 2::

    TYPE: POST
    URI: /api/v1/gameplay/ID/finish
    POST Parameters: None

GamePlay Finishing Examples
---------------------------------------------------------------

Finishing the *GamePlay* with *id* = *GAMEPLAY_ID*:

.. code-block:: bash

    $ curl --dump-header - -X POST \
    https://SERVER/api/v1/gameplay/GAMEPLAY_ID/finish/?api_username=USERNAME\&api_key=API_KEY

Possible Responses
---------------------------------------------------------------

The possible HTTP responses from the API are:

* HttpAccepted (202): The POST message was successful
* HttpBadRequest (400): You tried to finish an already finished GamePlay. GamePlay may just be finished once.
* HttpUnauthorized (401): Most probably there was a problem with the authentication of your USERNAME and API_KEY.
* HttpForbidden (403): If you try to finish a GamePlay which you didn't create, will raise a Forbidden Response. It is also possible that you wrote a wrong URL
* HttpNotFound (404): Wrong URL. Sometimes even a 200 OK code could be given with wrong information. It is very important that you check the URLs are exactly the same than in the examples.


.. Step Five: Send a Rawdata
    ----------------------------------------------------------------
    The last step. First create a file named :file:`rawdata.json`. Then copy this sample body::
        {
            "player_uuid" : "PPPP",
            "contentapp_uuid" : "ZZZZ",
            "gameplay_uuid" : "GGGG",
            "gameroute_uuid" : "RRRR",
            "screenplay_uuid" : "TTTT",
            "data:{}
        }
    You can send all this raw data to platform on every completed scene of the game (not incremental screen sending supported yet)::
        $curl --dump-header - -H "Content-Type: application/json" -X POST \
        --data @rawdata.json \
        "http://SERVER/api/v1/rawdata/?api_username=API_USERNAME&api_key=API_KEY&contentapp_uuid=ZZZZ"
        $HTTP/1.1 201 CREATED
         Server: nginx/1.2.2
         Date: Wed, 28 Nov 2012 21:07:08 GMT
         Content-Type: text/html; charset=utf-8
         Transfer-Encoding: chunked
         Connection: keep-alive
         Vary: Accept-Language, Cookie
         X-Frame-Options: SAMEORIGIN
         Location: https://SERVER/api/v1/rawdata/1/
         Content-Language: en
         Set-Cookie: sessionid=74f79a8bc60e882b4e06b7646a511ead; expires=Wed, 12-Dec-2012 21:07:08 GMT; httponly; Max-Age=1209600; Path=/; secure
         Set-Cookie: django_language=en; Path=/
    .. warning:: You MUST pass the GET parameter game_uuid in the URL or as a POST parameter. As a post parameter means NOT within the JSON body.\
     This does NOT mean that the body RawData parameter is enough. Authorization process needs game_uuid before JSON body is deserialized.\
     GET parameter as shown in the example above, ?api_username=API_USERNAME&api_key=API_KEY&game_uuid=ZZZZ, is the recommended way.
    All this data have been uploaded to platform and will be treated automatically.
    Step Five: Finishing the Game Play
    ----------------------------------------------------------------
    When the Game Play is finished you must provide this information by closing the game play with this method::
        $ curl --dump-header - "https://SERVER/api/v1/gameplay/finish/?id=2&api_username=API_USERNAME&api_key=API_KEY"
        $ HTTP/1.1 202 ACCEPTED
          Server: nginx/1.2.2
          Date: Thu, 29 Nov 2012 17:39:49 GMT
          Content-Type: application/json; charset=utf-8
          Transfer-Encoding: chunked
          Connection: keep-alive
          Vary: Accept-Language, Cookie
          X-Frame-Options: SAMEORIGIN
          Content-Language: en
          Set-Cookie: sessionid=10c4908b488e088ef72a77ed7782f390; expires=Thu, 13-Dec-2012 17:39:49 GMT; httponly; Max-Age=1209600; Path=/; secure
          Set-Cookie: django_language=en; Path=/
          {"success": true}
    If :file:`success=true` then the GamePlay has been successfully closed. All data related to this play's been processed.

If you received all the successful responses along the process, then your App and Infantium are ready to proceed
one step further. Congratulations! Get in contact with an Infantium representative for further instructions.

