.. _advanced-elements:

Elements
===============

Elements are the main reference objects in the data sent to the server by the SDK. They can represent persons,
animals, objects, numbers, images, text, or any other thing the kid can interact with, either actively or passively.
Knowing what the kid can see on the screen at the moment of performing any action is crucial to reach conclusions
about recurring patterns in the kids actions, just to name an example.

There are some parameters which are common to all kind of elements. Those are the *size*, *kinetic info* and *color*.
All of those attributes are optional, but are very useful to calculate cognitive information about the kid afterwards.
Here are some examples:

.. code-block:: java

    // Adding size to an element
    Element sized_element = new Element("balloon", 200, 100);
    infantium.addElement(sized_element);

    // Adding movement to an element
    Element moving_element = new Element("balloon");
    moving_element.set_movement("circular");
    infantium.addElement(moving_element);

    // Adding color to an element
    Element colored_element = new Element("balloon");
    colored_element.setRGBColor(255, 0, 0);
    infantium.addElement(colored_element);

Subtypes
-------------

As there are very different types of elements in the games and ebooks around the market, it is logical to have more
than one kind of *Element* in the Infantium SDK. Thus, in the following sections you will find different subtypes of
*Elements* which will allow you to better define your items with the least effort.

Number Elements
-------------------

Number elements are those related to cardinal or ordinal numbers, be it in the form of sets of elements, or the number
itself in arabic or text representation. This kind of element is always related to counting something, so it is very
easy to differentiate from other kinds of elements. This could be an example of a simple *Number Element*:

.. image:: /_static/game_screens/TutoToons_selection_goal_example.png

This element could be defined with a *NumberElement*. It takes an optional parameter named 'representations' explained
below:

.. code-block:: java

    // Add a number element with the fewest parameters
    NumberElement simple_number_element = new NumberElement("number_two", 2);
    infantium.addElement(simple_number_element);

    // An example of a full number with the optional parameter
    //  'representations'
    NumberElement full_number_element = new NumberElement("number_two", 2);
    full_number_element.add_representation("arabic");
    full_number_element.add_representation("set");
    infantium.addElement(full_number_element);

The representations parameter adds information to the number element, indicating in which way the number is transmitted
to the kid. The possible values can be:

* **arabic:** representation in arabic numbers like 1, 2, 3...
* **latin:** represeentation in latin numbers like I, II, III...
* **set:** representation as a set of elements which can be counted, like dots, or in the previous example, the wings.
* **length:** representation is also distinguishable by the length of the element. See the example below.

Representations can also have multiple values at the same time, and thus it also accepts Arrays as a parameter. This is
better seen in the following example:

.. image:: /_static/game_screens/Montessori_number_element.png

In this case, the element has two representations, one as an *arabic* number, and another one with both a *set* and a
*length* representation at the same time:

.. code-block:: java

    // Full NumberElement
    NumberElement full_number_element_2 = new NumberElement("number_two", 2);
    full_number_element_2.add_representation("arabic");
    full_number_element_2.add_representation(Arrays.asList("set", "length"));
    infantium.addElement(full_number_element_2);

    NumberElement full_number_element_6 = new NumberElement("number_six", 6);
    full_number_element_6.add_representation("arabic");
    full_number_element_6.add_representation(Arrays.asList("set", "length"));
    infantium.addElement(full_number_element_6);

Text Elements
-------------------

Text elements are very descriptive by themselves. They represent text on the screen, be it a single character or a
full sentence:

.. image:: /_static/game_screens/Teleport_torch_text_element.png

In this case, the upper text of the game would be represented as a *TextElement*:

.. code-block:: java

    // Add the sentence element
    TextElement sentence_element = new TextElement("help_text", "en-US",
        "MAKE A SHADOW PUPPET");
    infantium.addElement(sentence_element);

    // In another case, we may want to add just one character
    TextElement char_element = new TextElement("char_element", "a");
    infantium.addElement(char_element);

Shape Elements
-------------------

Shape elements are a special case of object on the screen for polygonal objects, which can fall into several categories,
for instance regular or irregular polygons. There is also a special parameter for star-shaped objects.

.. image:: /_static/game_screens/TutoToons_matching_goal_example.png

The previous elements could be defined as follows:

.. code-block:: java

    // One ShapeElement with the basic parameters
    ShapeElement square_element = new ShapeElement("square_elem", "square");
    infantium.addElement(square_element);

    // The star element has its own parameter, which is the 'n_sides'
    ShapeElement star_element = new ShapeElement("star_elem", "star", 5);
    infantium.addElement(star_element);

    // The final circle element
    ShapeElement circle_element = new ShapeElement("circle_elem", "circle");
    infantium.addElement(circle_element);

Picture Elements
-------------------

Picture elements refer to any real world picture that appears in a game, that is. It is a very straightforward element,
here you can see an example of *PictureElements*:

.. image:: /_static/game_screens/Category_conquest_picture_element.png

Here is an example of the code:

.. code-block:: java

    // Adding all the elements in the previous screen from an Array
    for (String element : screen_elements) {
        PictureElement simple_picture = new PictureElement(element);
        infantium.addElement(simple_picture);
    }

    // For Picture elements it is recommended to add the size too,
    //  but as most of the attributes, it is optional too
    PictureElement improved_picture = new PictureElement("dog", 150, 50);
    infantium.addElement(improved_picture);

Painted Elements
--------------------

Painted elements refer to any other kind of element either drawn by hand or by any software, that actually doesn't fall
in the previous definition for the *PictureElements*. An example:

.. image:: /_static/game_screens/TutoToons_multiple_matching_goal_example.png

In this case, all the flowers would be declared as *PaintedElements*:

.. code-block:: java

    // Adding all the elements in the previous screen from an Array
    for (String element : flower_list) {
        PaintedElement simple_drawing = new PaintedElement(element);
        infantium.addElement(simple_drawing);
    }

    // For Painted elements it is recommended to add the size too,
    //  as well as for PictureElements
    PaintedElement improved_drawing = new PaintedElement("cat", 150, 50);
    infantium.addElement(improved_drawing);

Generic Elements
--------------------

For any kind of element which you may consider does not fall into any of the previous categories, a generic *Element*
object is available too:

.. code-block:: java

    // Adding a generic Element with some extra information like size
    //  and movement
    Element random_element = new Element("happiness", 200, 100);
    random_element.set_movement("circular");
    infantium.addElement(random_element);

For more information about the Elements you can head to the `Elements Javadocs`_.



.. _Elements Javadocs: ../_static/javadocs/com/infantium/android/sdk/Element.html