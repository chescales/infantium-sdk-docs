
Installation
===============

As the SDK is delivered as a *jar* file, it is very easy to add to your project. Simply add it to your project
in a folder named *libs* and reference it from the build path. Don't forget to add the `dependencies`_ in the same
folder where the SDK is!

If you're using a specific framework instead of developing in native Android, you may have to add the plugin instead
of the SDK provided in the section before. Please refer to the `Plugins`_ section for more info.

Check installation
---------------------

To check the installation has worked properly, import the SDK from your App and check the version attribute of the SDK:

.. code-block:: java

    // Import the Android SDK
    import com.infantium.android.sdk.InfantiumSDK;

    // Inside your code get the version of the SDK
    Log.i(LOG_TAG, "Checking Infantium Installation! SDK Version: " + InfantiumSDK.version);
