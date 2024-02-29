# 99 Extra 04 Unit Tests


 <div id="moduleIndex">
  # Intro to Unit Tests
  An important part of coding is testing to see if your code is working correctly. Instead of asking a person to run the program each time it is changed to make sure it still runs properly, we can make much more reliable automated tests to check it out. These are known as unit tests.
  Test-driven development (TDD) is a way of developing code where you write the tests before you even start writing the program.  It’s a way to think through what your code must be able to do before your write it.
  ### JUnit Tests
  JUnit is an open source framework designed for the purpose of writing and running tests for java programs.

Tests can be written that specify the expected return value from running some code. 
    The syntax for the tests looks like this:
  assertEquals(expected, actual)
  If the "expected" value matches the "actual" value, the results bar displayed after running the tests will be green. If they are different (or there are errors), the results bar will be red.

For example, in the context of the "real world"
  assertEquals(true, Is water wet?)       results bar will be green

          assertEquals(true, Are zombies  real?)       results bar will be red

          assertEquals(false, Is coding lame?)       results bar will be green
  Now for some real code. Will the results bar be green or red for these asserts?
  assertEquals(4, add(2,2));

       assertEquals(“brains”, getZombieFood());

       assertEquals(2, getLargest(3,2));
 </div>

