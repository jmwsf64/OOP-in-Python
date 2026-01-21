# Project Introduction

This project is designed to illustrate the differences in the approaches between Procedural and Object-Oriented Programming.

Students will create a stick figure animation scene with Procedural code, and then create the same scene with Object-Oriented Programming.

More detail is provided in the `project-part-#.md` files.

# Part 1 - Procedural Approach

The `stickProdecural` module and `exampleSceneProcedural.py` are the starting points for the students.

Could the example scripts and function arguments and returns have been simplified? Absolutely! The point of this exercise is to illustrate the differences in the approaches of Procedural and Object-Oriented Programming.

### Module `stickProcedural`

The `stickProcedural` module contains three functions and a video renderer class.

###### `createCharacter`

This function accepts the `str` `sceneName`, `str` `charName`, and `int` `posx` arguments.

* `sceneName` is the json/avi file name that the character will be included in
* `charName` is the unique name of the character in the scene
* `posx` is the starting `x` position of the character's right foot. Must be greater than 0 and should be less than 1980

The function will create the scene json file if it does not exist and write a connectivity array to the json file under `charName`.

It will return 2-element `NumPy` arrays for each of the character animation points.

###### `rotateLimb`

This function accepts two 2-element `NumPy` arrays and a rotation angle. The first 2-element `NumPy` array acts as the fulcrum and the second array will be rotated around the first by the passed angle.

The function returns the new position of the second 2-element `NumPy` array.

Note that because this only rotates one point around another, if a character is going to, i.e., rotate their entire arm, both arm segments must be rotated individually.

###### `writeTime`

This function accepts the same `sceneName` and `charName` as the `createCharacter` function, the time to write in the scene file, and the individual 2-element `NumPy` arrays that make up the character.

This function will write each of the 2-element `NumPy` arrays to the scene file at the passed time, under the given character name

###### `class Render`

This class is used to create the animation set up by the students. Pass it the `sceneName` and it will create the animation based off the corresponding json file.

It also allows the user to write the first frame of the scene to a jpg file (`write_first_frame`) or display it using `cv2` (`show_first_frame`) to check their scene setup before rendering the scene to video.

### `exampleSceneProcedural-1`

This script creates a 10-second animation of a single character raising their arm 90 degrees. This is to demonstrate why more key points creates a smoother animation.

In the output video of this script, the character's arm will shorten and then lengthen again to make the rotation. Outputting more key points makes for a smoother animation but requires more effort in the script.

### `exampleSceneProcedural-2`

This script creates a 7-second animation of two characters waving at each other and will be a smoother animation than `exampleSceneProcedural-1`.

This script is meant to illustrate the procedural nature of procedural code. Students should feel welcome to use loops to simplify their work if they wish to do so. They must take care to properly track their time increment and angle increments for each individual character either way.

# Part 2 - OOP Approach

The `stickObject` module and `exampleSceneOOP.py` are the starting points for the students.

### Module `stickObject`

###### `class Person`

This class creates a stick figure person for the animation. During the object initialization it will write the `sceneName` and `charName` the same as the `createCharacter` function in the `stickProcedural` Module.

Each object will track its own points and keep track of its own time in the animation.

###### `class Render`

This is the same as the `Render` in the `stickProcedural` module.


###### `class Jason` and `class Mark`

These subclasses of `Person` are used to make sure that the 4 Principles of
Object-Oriented Programming are included in the project.

### `exampleSceneOOP`

This script creates the same 7-second waving animation as in `exampleSceneProcedural-2`.

Points to address to students for comparison:
* Each character tracks its own points and its own animation time
* We are no longer controlling each rotation of the limbs, we are giving the character an animation to perform and then the character takes care of it internally with the concept of encapsulation
* We can increase the number of key point outputs with a single argument change
  * In `exampleProcedural-2` it would have made our script's complexity increase exponentially
  * If we were using loops in that script it would not have been much more complex, but _we_ would still need to account for the change in time and angle in the script
* If we wanted to increase the number of points of our character it will increase the complexity of our `Person` class but not the main script
  * If we did the same in the procedural code it would increase the complexity in our functions and our script
  * This is an example of how Object-Oriented Programming can reduce complexity when scaling problems
* No matter how much simpler we can make the procedural scripts with loops, we must still pass each point to the `write_time` function individually and track them in our script
  * With the OOP code we do not need to do that because that information is always available to the character objects we create
* Note that in the procedural code we are essentially just managing different points and tracking them in the script as a character
  * In the OOP code, we are actually interacting with a character
  * We give the character animation commands and the character accomplishes them without us tracking each and every change
* The difference is further illustrated by printing the character
  * It will print out `Hi there! My name is <charName>!`
  * If we wanted to print out the character in the procedural example we would be printing out a series of points that we know create a character
