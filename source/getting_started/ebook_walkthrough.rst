.. _walkthroughs-ebook:

=====================================================
 Walkthrough: E-Book
=====================================================

:Date: |today|
:Revision: |release|
:Description: This tutorial show how to send an e-book rawdata, detailing the different required functions with its parameters.

Introduction
===========================

Dependencies
---------------------------

This SDK requires the library LoopJ v1.4.3 to be included in the project for proper functioning. You can find it in
the following link: `LoopJ Library 1.4.3`_

Android Permissions
---------------------------

The present SDK requires the following Android Permissions in the App manifest:

 - `INTERNET`_
 - `ACCESS_NETWORK_STATE`_

Singleton Pattern
---------------------------

Infantium_SDK has been created using a Singleton pattern, so the only way to get an instance of the class is by
calling the function: `getInfantium_SDK(Context context)`_. The SDK requires the *Context* of the Android Activity.

.. code-block:: java

 InfantiumSDK infantium = InfantiumSDK.getInfantiumSDK(this.getBaseContext());


The Handler
---------------------------

As most functions work asynchronously, an HttpHandler must be implemented. In order to simplify this task Infantium
created a class called *InfantiumAsyncResponseHandler* that provides the methods that must be implemented by the
Developers. Its methods are called after making a request to the API, such as creating a new player, getting logged
or sending an e-book rawdata.

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

In this example, if the user creates the *Gameplay* successfully, the SDK will call the `onSuccessCloseGameplay()`_.
If a problem comes up, it will call the `onFailureCloseGameplay(String description)`_. The description is a short
descriptive message that explains where or why the problem has arised.

Walkthrough
=====================

1. Configure the SDK
----------------------------------------

First of all, we have to configure the SDK with some data. This data will be, on one hand, the developer API
credentials for contacting with Infantium (`setDeveloperCredentials(String api_user, String api_key)`_). The other
function we should call is the `setDeviceInfo(w_dev, h_dev)`_ function in order to set the current device pixels.
Finally, if you want to receive feedback from the SDK, you will need to implement a Handler. This will be further
explained in the Handler section. You can do that with the `setDeveloperHandler(InfantiumAsyncResponseHandler handler)`_
function.

.. code-block:: java

   // Configure the SDK
   infantium.setDeveloperCredentials(api_user, api_key);
   infantium.setDeviceInfo(w_dev, h_dev);
   infantium.setDeveloperHandler(handler);


2. Set EBook ContentApp UUID
---------------------------------------------

The next step if to set the *contentapp_uuid*, which will identify the App against the server. To configure it the
method `setContentAppUUID(String contentapp_uuid)`_ should be used.

.. code-block:: java

   // Set the App contentapp_uuid
   infantium.setContentAppUUID(contentapp_uuid);

3. Set EBook Content UUID
---------------------------------------------

The method `setContentUUID(String content_uuid)`_ will set the EBook content UUID, required before creating a new
Gameplay.

.. code-block:: java

   // Set the Content's UUID
   infantium.setContentUUID(content_uuid);

If the content is not correct, the error will appear when calling the *sendEbookRawdata*.

4. Get Player UUID (from the Infantium App):
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

5. Create Gameplay:
----------------------------------------------

When we have set the *contentapp_uuid*, *content_uuid* and the *player_uuid* we can create a gameplay.

.. topic:: Function:

 `createGameplay()`_

.. NOTE:: the createGameplay(String subcontent_uuid, handler) is only used to create gameplays of games.

Possible responses:

 - *onSuccessCreateGameplay()*: The gameplay is created successfully.
 - *onFailureCreateGameplay(String description)*: If the player is not selected, the content is not informed or there is another gameplay opened

6. Rawdata Functions:
-------------------------------------

Once the gameplay is created, we can call the rawdata functions to introduce elements or sounds. Additionally, when the ebook page is shown (the kid can see the
objects in the screen), the function `startPlaying()`_ should be called. If any new elements, sounds or animations are displayed they can be added afterwards.

 - Required rawdata functions:

  - `addElement(Element element)`_
  - `addElements(List<Element> elements)`_
  - `addDynamicField(DynamicField d_field)`_
  - `addDynamicFields(List<DynamicField> d_fields)`_

7. Send Ebook Rawdata:
------------------------------

We finally call this function when we want to send the rawdata.

.. topic:: Function:

 `sendEbookRawData(int numPage, boolean text, boolean readToMe, final InfantiumAsyncResponseHandler responseHandler)`_
		
- numPage: The number of the page in the e-book.
- text - true if the page contains text or false if not.
- readToMe - true if the book reads to the player or false if not.

Possible responses:

 - *onSuccessEbookRawdata()*: The ebook rawdata is posted successfully.
 - *onFailureEbookRawdata(String description)*: A problem occurred when sending the ebook rawdata.

8. Close Gameplay
------------------------------

Last step but not least important. If the gameplay is not closed, the SDK will not be able to create new Gameplays.

.. topic:: Function:

 `closeGameplay(InfantiumAsyncResponseHandler handler)`_

Possible responses:

 - *onSuccessCloseGameplay()*: Gameplay closed succesfully.
 - *onFailureCloseGameplay(String description)*: If the gameplay is not started or another problem occurs when closing the gameplay.

.. _INTERNET: http://developer.android.com/reference/android/Manifest.permission.html#INTERNET
.. _ACCESS_NETWORK_STATE: http://developer.android.com/reference/android/Manifest.permission.html#ACCESS_NETWORK_STATE
.. _LoopJ Library 1.4.3: https://www.dropbox.com/s/sclmax88prirgk0/android-async-http-1.4.3.jar

.. _setDeviceInfo(w_dev, h_dev): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#setDeviceInfo(int,%20int)
.. _onFailureCloseGameplay(String description): ../_static/javadocs/com/infantium/android/sdk/InfantiumAsyncResponseHandler.html#onFailureCloseGameplay(java.lang.String)
.. _onSuccessCloseGameplay(): ../_static/javadocs/com/infantium/android/sdk/InfantiumAsyncResponseHandler.html#onSuccessCloseGameplay()
.. _getInfantium_SDK(Context context): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#getInfantium_SDK(android.content.Context)
.. _setDeveloperCredentials(String api_user, String api_key): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#setDeveloperCredentials(java.lang.String,%20java.lang.String)
.. _setDeveloperHandler(InfantiumAsyncResponseHandler handler): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#setDeveloperHandler(com.infantium.android.sdk.InfantiumAsyncResponseHandler)
.. _setContentAppUUID(String contentapp_uuid): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#setContentAppUUID(java.lang.String)
.. _setContentUUID(String content_uuid): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#setContentUUID(java.lang.String)
.. _createGameplay(String subcontent_uuid): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#createGameplay(java.lang.String)
.. _startPlaying(): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#startPlaying()

.. _Elements: ../_static/javadocs/com/infantium/android/sdk/Element.html
.. _Goals: ../_static/javadocs/com/infantium/android/sdk/Goal.html

.. _addElement(Element element): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#addElement(com.infantium.android.sdk.Element)
.. _addElements(List<Element> elements): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#addElements(java.util.List)
.. _addGoal(Goal goal): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#addGoal(com.infantium.android.sdk.Goal)

.. _addDynamicField(DynamicField d_field): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#addDynamicField(com.infantium.android.sdk.DynamicField)
.. _addDynamicFields(List<DynamicField> d_fields): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#addDynamicFields(java.util.List)

.. _newBasicInteraction(String t, String object_type, String goal_type): ../_static/javadocs/com/infantium/android/sdk/InfantiumSDK.html#newBasicInteraction(java.lang.String,%20java.lang.String,%20java.lang.String)

.. _sendGameRawData(): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#sendGameRawData()
.. _closeGameplay(): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#closeGameplay()

