.. _walkthroughs-game:

=====================================================
 Walkthrough: Game
=====================================================

:Author: Infantium <www.infantium.com>
:Date: $Date: 2013-09-20 01:10:53 +0000 (Wed, 20 Sep 2013) $
:Revision: $Revision: 1 $
:Description: This tutorial show how to send a game rawdata, detailing the different required functions with its parameters.

Introduction
===========================

Dependencies
---------------------------

This SDK requires the library LoopJ v1.4.3 to be included in the project for proper functioning. You can find it in the following link:
`LoopJ Library 1.4.3`_

Android Permissions
---------------------------

The present SDK requires the following Android Permissions in the App manifest:

 - `INTERNET`_
 - `ACCESS_NETWORK_STATE`_

Singleton Pattern
---------------------------

Infantium_SDK has been created using a Singleton pattern, so the only way to get an instance of the class is by calling the function:
`getInfantium_SDK(Context context)`_. The SDK requires the *Context* of the Android Activity.

.. topic:: Example:

 Infantium_SDK infantium = Infantium_SDK.getInfantium_SDK(this.getBaseContext());


The Handler
---------------------------

As most functions work asynchronously, an HttpHandler must be implemented. In order to simplify this task Infantium created a class called
*InfantiumAsyncResponseHandler* that provides the methods that must be implemented by the Developers. Its methods are called after making a
request to the API, such as creating a new player, getting logged or sending an e-book rawdata.

Here we can see an example of how to implement an *InfantiumasyncResponseHandler*:

.. code-block:: java

 InfantiumAsyncResponseHandler infantiumHandler = new InfantiumAsyncResponseHandler() {
		@Override
		public void onSuccessCloseGameplay(){
			System.out.println("---Gameplay closed successfully---");
		}

		@Override
		public void onFailureCloseGameplay(String description){
			System.out.println(description);
		}
 };

In this example, if the user creates the *Gameplay* successfully, the SDK will call the *onSuccessCloseGameplay()*. If a problem comes up,
it will call the *onFailureCloseGameplay(String description)*. The description is a short descriptive message that explains where or why the problem has arised.

Walkthrough
=====================

1. Configure the SDK
----------------------------------------

First of all, we have to configure the SDK with some data. This data will be, on one hand, the developer API credentials for contacting with Infantium.
The other function we should call is the *setDeviceInfo()* function in order to set the current device pixels

.. topic:: Function:

 `setDeveloperCredentials(String api_user, String api_key)`_

 `setDeviceInfo(w_dev, h_dev)`_

 `setDeveloperHandler(InfantiumAsyncResponseHandler handler)`_


2. Set Game ContentApp UUID
---------------------------------------------

We have to set the ContentApp UUID of the game before creating a gameplay.

.. topic:: Function:

 `setContentAppUUID(String contentapp_uuid)`_

Possible responses:

 - *onSuccessContentApp()*: the contentapp UUID has been found in the Infantium market.
 - *onFailureContentApp(String description)*: a problem occurred when trying to obtain the contentapp info from the market.

3. Get Player UUID (from the Infantium App):
----------------------------------------------
This function will get the UUID of the selected player in the InfantiumApp to be used by the SDK. This requires to add a few lines in the Android
Manifest of the App adapting to Infantium. The following receiver should be added to the Manifest:

.. code-block:: xml

    <receiver android:name="com.infantium.android.sdk.ReceivePlayer">
        <intent-filter>
            <action android:name="com.infantium.android.sdk.ReceivePlayer"></action>
        </intent-filter>
    </receiver>

This receiver should be added inside of the <application> tag of your Manifest. Once this is added, the call to get the Player (and this is the step 3) is:

.. topic:: Function:

 `getPlayerUUIDFromApp()`_

Possible responses:

 - *onSuccessGetPlayerByUUID()*: Player was successfully obtained, you can now proceed to the next step.
 - *onFailureGetPlayerByUUID(String description)*: A problem occurred while obtaining the player, check the description for more details.

4. Create Gameplay:
----------------------------------------------

When we have set the *contentapp_uuid* and the player_uuid we can create a *Gameplay*.

.. topic:: Function:

 `createGameplay(String subcontent_uuid)`_

.. NOTE:: the createGameplay() is only used to create gameplays of e-books.
.. NOTE:: Game gameplays can be created with an open e-book gameplay. Not vice versa.

Possible responses:

 - *onSuccessCreateGameplay()*: The gameplay is created successfully.
 - *onFailureCreateGameplay(String description)*: If the player is not selected, the content is not informed or there is another gameplay opened

 
5. Rawdata Functions:
-------------------------------------

Once the gameplay is created, we can call the rawdata functions to introduce elements or sounds. Additionally, when the game starts (the kid can see the objects
in the screen), the function `startPlaying()`_ should be called. If any new elements, sounds or animations are displayed they can be added afterwards. Nevertheless,
the elements already on the screen when the kid starts playing should be added before the *startPlaying* method invocation.

 - Required rawdata functions:

  - `addElement(Element element)`_
  - `addElements(List<Element> elements)`_
  - `tapNoObjects(List<Integer> position)`_
  - `tapNoObjects(List<Integer> position, String sound_id)`_
  - `tapOnObjects(String element_id)`_
  - `tapOnObjects(String element_id, String sound_id)`_
  - `setSuccesses(int successes)`_
  - `setFailures(int failures)`_

 - Optional rawdata functions:

  - `setTarget(Target target)`_
  - `setTargets(List<Target> targets)`_
  - `setEvaluate(List<String> eval)`_
  - `addSound(Sound sound)`_
  - `addSounds(List<Sound> sounds)`_
  - `addFixedAnimation(Animation animation)`_
  - `addFixedAnimations(List<Animation> animations)`_
  - `addDynamicField(DynamicField d_field)`_
  - `addDynamicFields(List<DynamicField> d_fields)`_
  - `startAnimation(String element_id, List<Integer> st_pos, String type)`_
  - `endAnimation(String element_id)`_
  - `endAnimation(String element_id, List<Integer> end_pos)`_
  - `endAnimation(String element_id, String sound_id, List<Integer> end_pos)`_
  - `startDragging(String element_id, List<Integer> position)`_
  - `finishDragging(List<Integer> position)`_
  - `finishDragging(List<Integer> position, int max_x, int max_y)`_
  - `finishDragging(List<Integer> position, String sound_id)`_
  - `finishDragging(List<Integer> position, String sound_id, int max_x, int max_y)`_

6. Send Game Rawdata:
------------------------------

We finally call this function when we want to send the rawdata.

.. topic:: Function:

 `sendGameRawData()`_

Possible responses:

 - *onSuccessGameRawdata()*: The game rawdata is posted successfully.
 - *onFailureGameRawdata(String description)*: A problem occurred when sending the game rawdata.

7. Close Gameplay
------------------------------

Last step but not least important. If the gameplay is not closed, the SDK will not be able to create new Gameplays.

.. topic:: Function:

 `closeGameplay()`_

Possible responses:

 - *onSuccessCloseGameplay()*: Gameplay closed succesfully.
 - *onFailureCloseGameplay(String description)*: If the gameplay is not started or another problem occurs when closing the gameplay.


.. _INTERNET: http://developer.android.com/reference/android/Manifest.permission.html#INTERNET
.. _ACCESS_NETWORK_STATE: http://developer.android.com/reference/android/Manifest.permission.html#ACCESS_NETWORK_STATE
.. _LoopJ Library 1.4.3: https://www.dropbox.com/s/o29qkzg44su0wzu/android-async-http-1.4.3.jar

.. _setDeviceInfo(w_dev, h_dev): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setDeviceInfo(int,%20int)
.. _onFailureCloseGameplay(String description): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/InfantiumAsyncResponseHandler.html#onFailureCloseGameplay(java.lang.String)
.. _getInfantium_SDK(Context context): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#getInfantium_SDK(android.content.Context)
.. _setDeveloperCredentials(String api_user, String api_key): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setDeveloperCredentials(java.lang.String,%20java.lang.String)
.. _setDeveloperHandler(InfantiumAsyncResponseHandler handler): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setDeveloperHandler(com.infantium.android.sdk.InfantiumAsyncResponseHandler)
.. _setContentAppUUID(String contentapp_uuid): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setContentAppUUID(java.lang.String)
.. _setContentUUID(String ebook_content_uuid): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setContentUUID(java.lang.String)
.. _getPlayerUUIDFromApp(): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#getPlayerUUIDFromApp()
.. _createGameplay(String subcontent_uuid): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#createGameplay(java.lang.String)
.. _startPlaying(): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#startPlaying()

.. _addElement(Element element): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addElement(com.infantium.android.sdk.Element)
.. _addElements(List<Element> elements): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addElements(java.util.List)
.. _tapNoObjects(List<Integer> position): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapNoObjects(java.util.List)
.. _tapNoObjects(List<Integer> position, String sound_id): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapNoObjects(java.util.List,%20java.lang.String)
.. _tapOnObjects(String element_id): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapOnObjects(java.lang.String)
.. _tapOnObjects(String element_id, String sound_id): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapOnObjects(java.lang.String,%20java.lang.String)
.. _setSuccesses(int successes): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setSuccesses(int)
.. _setFailures(int failures): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setFailures(int)

.. _setTarget(Target target): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setTarget(com.infantium.android.sdk.Target)
.. _setTargets(List<Target> targets): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setTargets(java.util.List)
.. _setEvaluate(List<String> eval): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setEvaluate(java.util.List)
.. _addSound(Sound sound): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addSound(com.infantium.android.sdk.Sound)
.. _addSounds(List<Sound> sounds): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addSounds(java.util.List)
.. _addFixedAnimation(Animation animation): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addFixedAnimation(com.infantium.android.sdk.Animation)
.. _addFixedAnimations(List<Animation> animations): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addFixedAnimations(java.util.List)
.. _addDynamicField(DynamicField d_field): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addDynamicField(com.infantium.android.sdk.DynamicField)
.. _addDynamicFields(List<DynamicField> d_fields): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addDynamicFields(java.util.List)
.. _startAnimation(String element_id, List<Integer> st_pos, String type): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#startAnimation(java.lang.String,%20java.util.List,%20java.lang.String)
.. _endAnimation(String element_id): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#endAnimation(java.lang.String)
.. _endAnimation(String element_id, List<Integer> end_pos): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#endAnimation(java.lang.String,%20java.util.List)
.. _endAnimation(String element_id, String sound_id, List<Integer> end_pos): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#endAnimation(java.lang.String,%20java.lang.String,%20java.util.List)
.. _startDragging(String element_id, List<Integer> position): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#startDragging(java.lang.String,%20java.util.List)
.. _finishDragging(List<Integer> position): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.List)
.. _finishDragging(List<Integer> position, int max_x, int max_y): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.List,%20int,%20int)
.. _finishDragging(List<Integer> position, String sound_id): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.List,%20java.lang.String)
.. _finishDragging(List<Integer> position, String sound_id, int max_x, int max_y): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.List,%20java.lang.String,%20int,%20int)

.. _sendGameRawData(): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#sendGameRawData()
.. _closeGameplay(): http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#closeGameplay()
