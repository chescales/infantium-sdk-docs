.. _walkthroughs-ebook:

=====================================================
 Walkthrough: E-Book
=====================================================
:Author: Infantium <www.infantium.com>
:Date: $Date: 2013-09-20 01:10:53 +0000 (Wed, 20 Sep 2013) $
:Revision: $Revision: 1 $
:Description: This tutorial show how to send an e-book rawdata, detailing the different required functions with its parameters.

Introduction
===========================

Singleton pattern
---------------------------
Infantium_SDK has been created using a Singleton pattern, so the unique way to get an instance of the class is by calling the function: `.getInfantium_SDK() <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#getPlayerList()>`_.

.. topic:: Example:

 Infantium_SDK infantium = Infantium_SDK.getInfantium_SDK();
 
.. topic:: Tip:

 The device dimensions are used in the majority of the functions of the Infantium_SDK class. 
 We highly recommend calling the `.setDeviceInfo(w_dev,h_dev) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setDeviceInfo(int,%20int)>`_ after getting an instance of the class.

The Handler
---------------------------
The majority of this functions work asynchronously, so an HttpHandler must be implemented. In order to simplify this task. 

Infantium created a class called InfantiumAsyncResponseHandler that provides the methods that must be implemented by the Developers.

This methods are called after making a request to the API, such as creating a new player, getting logged or send an e-book rawdata. 

Here we can see an exemple of how to implement an InfantiumasyncResponseHandler: 
::

 .closeGameplay( new InfantiumAsyncResponseHandler(){
		@Override
		public void onSuccessCloseGameplay(){
			System.out.println("---Gameplay closed successfully---");
		}
		
		@Override
		public void onFailureCloseGameplay(String description){
			System.out.println(description);
		}
 });
	
In this example, if the user gets logged successfully, the SDK will call the onSuccessCloseGameplay(). If a problem comes up, will call the onFailureCloseGameplay(String description). 
The description is a short descriptive message that explains where or why has the problem came up.

Walkthrough
=====================

1. Set Developer credentials
------------------------------ 
First of all, we have to update our Developer credentials in order to contact with the API.
  
.. topic:: Function:

 `.setDeveloperCredentials(String api_user,String api_key) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setDeveloperCredentials(java.lang.String,%20java.lang.String)>`_

2. Set e-book ContentApp UUID
---------------------------------------------
We have to set the ContentApp UUID of the e-book before creating a gameplay.

.. topic:: Function:

 `.setContentAppUUID(String ebook_contentapp_uuid, handler) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setContentAppUUID(java.lang.String,%20com.infantium.android.sdk.InfantiumAsyncResponseHandler)>`_

Possible responses:

 - onSuccessContentApp(): the contentapp UUID is found in the Infantium market.
 - onFailureContentApp(String description): a problem ocurred when trying to obtain the contentapp info from the market.

3. Set e-book Content UUID
---------------------------------------------
This function will set the ebook content UUID, required before creating a new Gameplay.

.. topic:: Function:

 `.setContentUUID(String ebook_content_uuid) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setContentUUID(java.lang.String)>`_

If the content is not correct, the error will appear when calling the sendEbookRawdata.

4. Set Player UUID:
----------------------------------------------
This function will set the UUID of the selected player.

.. topic:: Function:

 `.setPlayerUUID(String player_uuid, InfantiumAsyncResponseHandler handler) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setPlayerUUID(java.lang.String,%20com.infantium.android.sdk.InfantiumAsyncResponseHandler)>`_
 
Possible responses:

 - onSuccessGetPlayerByUUID(): the player was succesfully found int the Infantium DB.
 - onFailureGetPlayerByUUID(String description): a problem ocurred when trying to obtain the info from the player or the related tutor.

5. Create Gameplay:
----------------------------------------------
When we have set the contentapp_uuid, content_uuid and the player_uuid we can create a gameplay.

.. topic:: Function:

 `.createGameplay(InfantiumAsyncResponseHandler handler) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#createGameplay(com.infantium.android.sdk.InfantiumAsyncResponseHandler)>`_

.. NOTE:: the .createGameplay(String subcontent_uuid, handler) is only used to create gameplays of games.

Possible responses:

 - onSuccessCreateGameplay: The gameplay is created succesfully.
 - onFailureCreateGameplay(String description): If the player is not selected, the content is not informed or there is another gameplay opened

6. Rawdata Functions:
-------------------------------------
Once the gameplay is created and the game is started, we can call the rawdata functions. Some of them are required when sending the ebook rawdata.

 - Required rawdata functions:

  - `.addElement(Element element) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addElement(com.infantium.android.sdk.Element)>`_
  - `.addElements(List<Element> elements) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addElements(java.util.ArrayList)>`_
  - `.tapNoObjects(ArrayList<Integer> position) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapNoObjects(java.util.ArrayList)>`_
  - `.tapNoObjects(ArrayList<Integer> position, String sound_id) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapNoObjects(java.util.ArrayList,%20java.lang.String)>`_
  - `.tapOnObjects(String element_id) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapOnObjects(java.lang.String)>`_
  - `.tapOnObjects(String element_id, String sound_id) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#tapOnObjects(java.lang.String,%20java.lang.String)>`_
  - `.setTarget(Target target) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setTarget(com.infantium.android.sdk.Target)>`_
  - `.setTargets(List<Target> targets) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setTargets(java.util.ArrayList)>`_
  - `.setSuccesses(int successes) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setSuccesses(int)>`_
  - `.setFailures(int failures) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#setFailures(int)>`_

 - Optional rawdata functions:

  - `.addSound(Sound sound) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addSound(com.infantium.android.sdk.Sound)>`_
  - `.addSounds(List<Sound> sounds) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addSounds(java.util.ArrayList)>`_
  - `.addFixedAnimation(Animation animation) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addFixedAnimation(com.infantium.android.sdk.Animation)>`_
  - `.addFixedAnimations(ArrayList<Animation> animations) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#addFixedAnimations(java.util.ArrayList)>`_
  - `.startAnimation(String element_id, ArrayList<Integer> st_pos, String type) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#startAnimation(java.lang.String,%20java.util.ArrayList,%20java.lang.String)>`_
  - `.endAnimation(String element_id) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#endAnimation(java.lang.String)>`_
  - `.endAnimation(String element_id, ArrayList<Integer> end_pos) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#endAnimation(java.lang.String,%20java.util.ArrayList)>`_
  - `.endAnimation(String element_id, String sound_id, ArrayList<Integer> end_pos) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#endAnimation(java.lang.String,%20java.lang.String,%20java.util.ArrayList)>`_
  - `.startDragging(String element_id, ArrayList<Integer> position) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#startDragging(java.lang.String,%20java.util.ArrayList)>`_
  - `.finishDragging(ArrayList<Integer> position) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.ArrayList)>`_
  - `.finishDragging(ArrayList<Integer> position, int max_x, int max_y) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.ArrayList,%20int,%20int)>`_
  - `.finishDragging(ArrayList<Integer> position, String sound_id) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.ArrayList,%20java.lang.String)>`_
  - `.finishDragging(ArrayList<Integer> position, String sound_id, int max_x, int max_y) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#finishDragging(java.util.ArrayList,%20java.lang.String,%20int,%20int)>`_

7. Send Ebook Rawdata:
------------------------------
We finally call this function when we want to send the rawdata. It is automatically send when closing gameplay if it is not sent before.

.. topic:: Function:

 `.sendEbookRawData(int numPage, boolean text, boolean readToMe, final InfantiumAsyncResponseHandler responseHandler) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#sendEbookRawData(int,%20boolean,%20boolean,%20com.infantium.android.sdk.InfantiumAsyncResponseHandler)>`_
		
- numPage: The number of the page in the e-book.
- text - true if the page contains text or false if not.
- readToMe - true if the book reads to the player or false if not.

Possible responses:

 - onSuccessEbookRawdata: The ebook rawdata is posted succesfully.
 - onFailureEbookRawdata(String description): A problem ocurred when sending the e-book rawdata.

8. Close Gameplay
------------------------------
Last step but not least important. If the gameplay is not closed, the SDK would not be able to create new Gameplays.

.. topic:: Function:

 `.closeGameplay(InfantiumAsyncResponseHandler handler) <http://docs.infantium.com/sdk/android/com/infantium/android/sdk/Infantium_SDK.html#closeGameplay(com.infantium.android.sdk.InfantiumAsyncResponseHandler)>`_

Possible responses:

 - onSuccessCloseGameplay(): Gameplay closed succesfully.
 - onFailureCloseGameplay(String description): If the gameplay is not initied or another problem ocurred when closing the gameplay.