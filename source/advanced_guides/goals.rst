.. _goals:

Goals
=========

Knowing the :ref:`elements<Elements>` on the screen is crucial for our analysis, but all of it would lack a real value
if we didn't know what are the micro-objectives in the current activity the kid is playing, and of course the final
goal. Knowing **what the kid has to do** is as important as knowing **what the kid actually does**. Knowing what the
kid has to do is what Goals are for.

Subtypes
-------------

There are several classes of *Goals*, depending on the final objective of each activity. To make it clearer in the SDK,
developers can choose from different implementations of the Goal class, which are explained below.

Selection Goals
--------------------

A selection goal object is used whenever the objective requires the kid to select an item from a list of possible
elements, where some of them (or all except one) are incorrect. In the following example only one element is correct:

.. image:: /_static/game_screens/TutoToons_selection_goal_example.png

For this activity we would use the *SelectionGoal* class. All of the following are valid examples:

.. code-block:: java

    // A simple Goal with just a goal name.
    //  The 'unique_solution' parameter is true by default
    SelectionGoal simple_two_wings_goal = new SelectionGoal("two_wings_goal");
    infantium.addGoal(simple_two_wings_goal);

    // An improved SelectionGoal with some optional parameters
    //  'name', 'unique_solution', and number of 'correct' and 'incorrect' choices.
    SelectionGoal improved_two_wings_goal = new SelectionGoal("two_wings_goal", true);
    improved_two_wings_goal.set_n_correct_choices(1);
    improved_two_wings_goal.set_n_incorrect_choices(2);
    infantium.addGoal(improved_two_wings_goal);

    // A full SelectionGoal with all the optional parameters
    //  'name', 'unique_solution', 'needed_action', 'correct' and 'incorrect' choices.
    SelectionGoal full_two_wings_goal = new SelectionGoal("two_wings_goal", true, "tap");
    full_two_wings_goal.set_correct_choices(Arrays.asList("two_wings_element"));
    full_two_wings_goal.set_incorrect_choices(Arrays.asList("one_wing_element",
        "three_wings_element"));
    infantium.addGoal(full_two_wings_goal);

Matching Goals
--------------------

In other kind of games, the kid is required to match one element with a target, usually corresponding to elements
and their shadowed silhouettes, or puzzle pieces into a shadow of the resolved image or just an empty space. For instance:

.. image:: /_static/game_screens/TutoToons_matching_goal_example.png

In these cases the *MatchingGoal* is the most appropriate class:

.. code-block:: java

    // A simple Goal with just a goal name and the 'matching_element' parameter
    MatchingGoal simple_select_key_goal = new MatchingGoal("key_goal_1", "squared_element");
    infantium.addGoal(simple_select_key_goal);

    // A full MatchingGoal with the optional parameters 'target_element' and 'correspondence_type'
    MatchingGoal full_select_key_goal = new MatchingGoal("key_goal_1", "squared_element",
        "squared_shadow_element");
    full_select_key_goal.add_correspondence_type("shape");
    full_select_key_goal.add_correspondence_type("size");
    infantium.addGoal(full_select_key_goal);

However, there are some game activities where the kid can match different elements among them, where for a given
target multiple elements fit as the correct solution, for instance the following activity, where all the flowers fit
each of the targets:

.. image:: /_static/game_screens/TutoToons_multiple_matching_goal_example.png

In this case you can add a list of element IDs that fit the same target, or even use the keyword "*ALL*" to mark that
all the elements can fit that target. An example of the code:

.. code-block:: java

    // The same previous Goal with just a goal name and a list of 'matching_element' ids
    //  as a parameter
    MatchingGoal multiple_select_key_goal = new MatchingGoal("key_goal_1",
        Arrays.asList("flower_1", "flower_3", "flower_5"));
    infantium.addGoal(multiple_select_key_goal);

    // A full MatchingGoal with the optional parameters 'target_element' and 'correspondence_type'
    //  which can accept ALL elements as correct elements
    MatchingGoal full_multiple_select_key_goal = new MatchingGoal("key_goal_1", "ALL",
        "flower_spot_element_1");
    full_multiple_select_key_goal.add_correspondence_type("shape");
    full_multiple_select_key_goal.add_correspondence_type("size");
    infantium.addGoal(full_multiple_select_key_goal);

Tapping Goals
---------------

A tapping goal is a kind of goal where the kid just has to tap on the elements he's seeing, without making any
distinction of the nature of the element, i.e., all elements need to be tapped. An example could be:

.. image:: /_static/game_screens/TutoToons_tapping_goal_example.png

In this case, there is an object named *TappingGoal* which adapts to this scenario:

.. code-block:: java

    // A TappingGoal with the least parameters
    TappingGoal simple_tapping_goal = new TappingGoal("tap_odd_flies",
        Arrays.asList("fly_1", "fly_3", "fly_5"));
    infantium.addGoal(simple_tapping_goal);

    // The "ALL" parameter can be used here too
    TappingGoal simple_tapping_goal = new TappingGoal("tap_all_flies", "ALL");
    infantium.addGoal(simple_tapping_goal);

If it is possible to give more information about the nature of the elements on the screen, it can be done by
specifying the type of those elements with an additional *type* parameter, which can take the values: "*moving*" for
dynamic elements, "*highlighted*" for elements which stand out intentionally from the rest of the elements, or "*hidden*"
for partially hidden elements.

.. code-block:: java

    // A TappingGoal with the least parameters
    TappingGoal moving_tapping_goal = new TappingGoal("tap_all_flies", "ALL", "moving");
    infantium.addGoal(moving_tapping_goal);

Generic Goals
--------------------

There are some kind of goals which do not fall inside any of the previous sutbypes. For those kind of objectives the
generic Goal should be enough to describe the nature of the activity. For instance the following painting game:

.. image:: /_static/game_screens/TutoToons_generic_goal_example.png

The previous activity could be defined with the default *Goal* class:

.. code-block:: java

    // A Goal with the least parameters
    Goal painting_goal = new Goal("paint_the_elephant");
    infantium.addGoal(painting_goal);

    // A full Goal with all the optional parameters:
    //  'time_limit' (in milliseconds),
    //  'instructions' referencing to an element id of the help text,
    //  'auto_eval' which describes if the action automatically triggers
    //    the evaluation process or not
    Goal full_painting_goal = new Goal("paint_the_elephant", 10000, true);
    full_painting_goal.set_instructions("instructions_element");
    infantium.addGoal(full_painting_goal);

For more information about the Goals you can head to the `Goal Javadocs`_.


.. _Goal Javadocs: ../_static/javadocs/com/infantium/android/sdk/Goal.html