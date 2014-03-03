.. _walkthroughs-ebook:

=====================================================
 Walkthrough: E-Book
=====================================================

:Date: |today|
:Revision: |version|
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

4. Create Gameplay:
----------------------------------------------

When we have set the *contentapp_uuid* and the *content_uuid* we can create a *Gameplay* with: `createGameplay()`_.

.. code-block:: java

   // Create the Gameplay
   infantium.createGameplay();

5. Rawdata Functions:
-------------------------------------

The *GamePlay* is created once every time the kid starts a reading session. Now, for every activity played or page
turned during that time, a *RawData* object is sent, which will contain the information we need to analyze. This contains,
among other generic stats, the elements in the screen and the goals to achieve, and finally the actions the kid performs.

When the kid enters one of the activities of the ebook (i.e. starts reading the ebook), the *RawData* is filled in three
phases:

1. Register the elements in the screen.

 This is done adding the `Elements`_ in the screen (`addElement(Element element)`_) and the `Goals`_ the kid has to
 complete to succeed in this game (`addGoal(Goal goal)`_).

 An example *Element* could be:

 .. code-block:: java

    // Add an element for a dog
    PaintedElement dog_element = new PaintedElement("dog_figure");
    infantium.addElement(dog_element);

    // A ball
    PaintedElement ball_element = new PaintedElement("ball");
    infantium.addElement(ball_element);

    // Add a number element
    NumberElement number_three = new NumberElement(3);
    infantium.addElement(number_three);

    // Add a text element
    TextElement sentence_element = new TextElement("en-US",
        "This little puppy wants to play with the ball! Can you help him?");
    infantium.addElement(sentence_element);

 An example *Goal* could be:

 .. code-block:: java

    // The Goal is to move the ball to the dog
    Goal g = new Goal("drag_the_ball", "selection");
    infantium.addGoal(g);


2. Start the timers and register the actions of the kid.

 When the kid starts interacting with the screen, we will call the `startPlaying()`_ method. This will trigger the
 timers inside the SDK. The SDK will automatically handle the timestamps when the kid taps the screen and the elements
 show up, which will allow us to get a lot of statistics about the child's development, relieving the developer of
 that task.

 For each time the kid interacts with the screen, this can be registered with the
 `newBasicInteraction(String t, String object_type, String goal_type)`_ method.
 In this method, the *t* equals to the type of the interaction, which can be *"success"*, *"failure"*, *"none"* or some others
 explained in the *BasicInteraction* section.

 .. code-block:: java

    // Dragging the ball to the dog is the goal of the activity,
    //  and thus it is represented a "success".
    InfantiumResponse res = infantium.newBasicInteraction("success", "ball", "drag_the_ball");

    // Another example, if the kid drags the "smartphone" element,
    //  but was not the goal of this activity.
    infantium.newBasicInteraction("error", "smartphone", "drag_the_ball");

6. Send Ebook Rawdata:
------------------------------

We finally call `sendEbookRawData(int numPage, boolean text, boolean readToMe)`_ when we want to send the *RawData*.
After sending the data, and the kid starts a new activity/page, the flow would go again to the 4th step!
If the kid goes back to the main menu, proceed to step 6.

.. code-block:: java

    // Send the previously introduced data
    infantium.sendEbookRawData(1, true, false);

We finally call this function when we want to send the rawdata.

7. Close Gameplay
------------------------------

Last step but not least important: `closeGameplay()`_. If the *GamePlay* is not closed, the SDK will not be able to
create new ones.

8. Conclusions
---------------

And with this the full cycle for sending data is complete. The integration can be enriched with many more methods and
variables, but we hope this gave you an insight of the process to integrate your ebooks with Infantium!

Now you can refer to the :ref:`advanced-guides` section for more info.

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

.. _sendEbookRawData(int numPage, boolean text, boolean readToMe): ../_static/javadocs/com/infantium/android/sdk/InfantiumSDK.html#sendEbookRawData(int,%20boolean,%20boolean)
.. _closeGameplay(): ../_static/javadocs/com/infantium/android/sdk/Infantium_SDK.html#closeGameplay()

