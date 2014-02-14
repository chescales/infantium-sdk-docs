=====================================================
 Adding the Infantium Button
=====================================================

:Date: |today|
:Revision: |release|
:Description: This section shows how to add the Infantium Button to your App.

Downloading
===============

The button graphics may be downloaded from `the following link`_. Here is an example of the button:

.. image:: _static/return_button_infantium.png

Positioning
===============

The Infantium button should be placed in the main screens of the game, this is, where the user selects which games
to play. It should also be included in the landing screen where the user first stops after launching the game.

Calling the SDK
================

The function of the SDK to be called is `returnToInfantiumApp()`_ with the current activity as the only parameter.
This will open the Infantium App from which your App was called.

.. _the following link: https://www.dropbox.com/s/065uqdqcyg4ohyw/return_button_infantium.png
.. _returnToInfantiumApp(): http://android.sdk.infantium.com/com/infantium/android/sdk/Infantium_SDK.html#returnToInfantiumApp(android.app.Activity)