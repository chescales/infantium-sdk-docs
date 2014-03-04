.. _advanced-interactions:

Basic Interactions
=====================

As you may guess, the set of interactions of the kid with the screen is one of the cornerstones of our analysis. Being
as important as it is for us, we want to make that interaction as simple as possible while keeping it meaningful for us.
That is why we have tried to make it a simple interaction of the developers with the SDK. This kind of interactions
is managed by the concept named *Basic Interaction*.

*Basic Interactions* capture what the kid is doing with the screen, regarding both the action itself, and the meaning
of the action for the current activity at the app. Below you can find a simple example to start with:

.. code-block:: java

    // Dragging the ball to the dog is the goal of the activity,
    //  and thus it is represented a "success".
    InfantiumResponse res = infantium.newBasicInteraction("success", "ball", "drag_the_ball");

    // Another example, if the kid drags the "smartphone" element,
    //  but was not the goal of this activity.
    infantium.newBasicInteraction("error", "smartphone", "drag_the_ball");



