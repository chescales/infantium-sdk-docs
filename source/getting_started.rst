======================
Getting Started
======================

So what now? When speaking about integrating a game with Infantium many developers get a little bit confused. Integrating
a game with Infantium means communicating with our SDK at different points of your Apps, feeding it with three different
core sources of information, which are where we extract the data for our Cognitive Analysis:

* The *Elements* on the screen.
* The *Goals* (or objectives) that the kid must achieve.
* The actual *Interactions* that happen during game time.

To do this there are a series of methods to be called at different parts of your code. For instance, the Elements and
Goals will probably be declared at the beginning of your game scenes (when the visual aspects of the current activity
are declared), whereas the Interactions will very likely be captured at the Event handlers your code may implement to
decide whether a kid has performed correctly an activity or not.

To make the smoothest first contact between the developers and the SDK, we have prepared two Walkthroughs which will
drive you through the basics of the full integration of an App. Additionally, all the apps would have to implement also
both the :ref:`Adding the Infantium Button <adding-button>` and the :ref:`Overriding the Android Cycle <android-cycle>`
guides.

Check out the following guides on how to integrate E-Books and Games!

.. toctree::
    :maxdepth: 1

    getting_started/game_walkthrough.rst
    getting_started/ebook_walkthrough.rst

.. getting_started/activity_cycle.rst