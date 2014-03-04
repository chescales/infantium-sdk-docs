
Overriding the Android Cycle
===================================

The SDK needs to execute some logic at the moment of creation and destruction of the contents adapted to Infantium, as
well as at the moment of resuming and pausing those contents. To fully understand this, in case the native methods
*onResume* and *onPause* are not familiar to you, you should check out the `Android Activity Lifecycle`_ page.

Once this is clear, those methods can be easily overwritten from your App by setting your own *onResume* and *onPause*
which call their parent methods from your Activity. Inside those methods then it is where you should call the Infantium
SDK methods that will take care of leaving your app in a consistent method. This is because many apps in the same
tablet will be using the SDK, and it is important there are no receivers active from one app that could interfere with
the others. All you have to do is overwrite the native methods and call the SDK functions. Here is an example of the
code that would achieve this goal:

.. code-block:: java

    @Override
        protected void onResume() {
            super.onResume();
            Log.i("Your-App-Tag", "--- Resumed MainActivity ---");  // Just for example purposes
            infantium.onResumeInfantium();
    }

    @Override
    protected void onPause() {
            super.onPause();
            Log.i("Your-App-Tag", "--- Paused MainActivity ---");  // Just for example purposes
            infantium.onPauseInfantium();
    }

With these simple two functions of two lines each (you can avoid the comments), the app will seamlessly integrate with
other apps in the same tablet with Infantium, both at creation/destruction and at resuming/pausing!

.. _Android Activity Lifecycle: http://developer.android.com/reference/android/app/Activity.html#ActivityLifecycle
