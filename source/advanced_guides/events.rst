.. _advanced-events:

Events
===============

In the version 2.3 of the SDK we have introduced the *Events* figure, which will allow developers to register the
different types of events that may happen during the playing time of the kid with their content. The first batch of
events include two different types, apart from the *generic events*, and those are *Sound Events* and *Missed Opportunities*.

Declaring and Triggering Events
---------------------------------

The *Events* section of the SDK differentiates two steps in the events area: declaring an event once, and triggering
it as many times as it happens in the game. Thus, there are two main parts in this section, `Declaring Events`_ and
`Triggering Events`_.

Declaring Events
------------------

The first step of process is to declare the *Events* that may happen during the current scene. They are declared at the
same time of the :ref:`Elements <advanced-elements>` and :ref:`Goals <advanced-goals>`. There is a *Generic Event*
which can be used to declare *Events* that do not fall in the specific types. The specific types are explained afterwards.

Generic Events
^^^^^^^^^^^^^^^^

Generic events do not give much information, as they do not specify which kind of event the kid is seeing. Nevertheless,
they are useful for us as they allow our analytic system to know if there is any kind of reward the kid is having after
performing the different actions on the screen, and thus that is important data to take into account when analyzing
the different interactions declared during play time.

Here is the example code:

.. code-block:: java

	// Add a simple generic event with its ID
	Event ev = new Event("sun_starts_shining");
	InfantiumResponse res = infantium.addEvent(ev);

Sound Events
^^^^^^^^^^^^^^

When an event represents a sound being played at a specific time or after a specific action, this should be registered
with the *SoundEvent* class. This event is very useful for us, as it may include the text read, the language of the text,
the sound or song which may be sung, etc. We can know how many times a kid has been exposed to a previous concept before
the current game, so we greatly encourage developers to register this kind of events!

.. image:: /_static/game_screens/MyFirstWords_sound_events.png

In the previous example, every time the kid taps on one of the *Elements* on the screen, he can hear the name of the
animal he is touching. In this example, one *SoundEvent* would be declared per *Element* on the screen, and it would
be *Triggered* every time the kid taps on the picture (explained in the next subsection).

.. code-block:: java

	// Add a simple Sound Event
	SoundEvent ev1 = new SoundEvent("lion_name_sound_basic");
	InfantiumResponse res1 = infantium.addEvent(ev1);

	// It is also recommended to add the text and type of Sound:
	SoundEvent ev2 = new SoundEvent("lion_name_sound_w_text", "voice");
	ev2.set_associated_text("Lion", "en-US");
	InfantiumResponse res2 = infantium.addEvent(ev2);

	// We allow also to reuse other text elements used before
	// (for example instructions in the games)
	TextElement help_text_element = new TextElement("help_text", "en-US",
		"MAKE A SHADOW PUPPET");
	infantium.addElement(help_text_element);
	SoundEvent ev3 = new SoundEvent("lion_name_sound_with_element", "voice",
		"help_text_element");
	InfantiumResponse res3 = infantium.addEvent(ev3);

	// Add a full Sound Event with the optional parameters
	//  imprecise_sound_volume: the approximate sound level
	//  duration: the milliseconds of duration of the sound
	SoundEvent ev4 = new SoundEvent("full_lion_name_sound_w_text", "voice");
	ev4.set_associated_text("Lion", "en-US");
	ev4.set_imprecise_sound_volume(0.5);
	ev4.set_duration(5000L);
	InfantiumResponse res4 = infantium.addEvent(ev4);

Triggering Events
------------------

The second part of this section is triggering the events as soon as they occur in the current scene. This is very simple,
it just requires developers to make a call to the `triggerExistingEvent(String event_id)`_ method in the event handlers
of your code. Here you can find an example for triggering the events declared in the previous section:

.. code-block:: java

	// Trigger the first Generic Event
	InfantiumResponse res = infantium.triggerExistingEvent("sun_starts_shining");

	// Trigger one of the previous Lion Sound Events.
	//  triggered_by parameter indicates what triggered the event
	InfantiumResponse res = infantium.triggerExistingEvent("lion_name_sound_w_text", "tap");

For more information about the Events you can head to the `Events Javadocs`_.


.. _triggerExistingEvent(String event_id):
.. _Events Javadocs:
