# 01 Intro To Static


 <div id="moduleIndex">
  # Running Race - Explaining Static
  The static keyword is a reserved word in Java like int, for, if, and else.
  It can be placed before the type when declaring member variables:
  ```

static int var = 1;
static Robot rob;
    
```
  and before the return type for method definitions:
  ```

static float calculateArea(float width, float height){ // code }
public static void main(String[] args){ // code }
    
```
  ### 1. Static Variable Lifetime
  A member variable without static
  <b>
   DOES NOT
  </b>
  exist before an object/instance of a class is made.
  A member variable with static
  <b>
   DOES
  </b>
  exist before an object/instance of a class is made.
  Take the Athlete class for example:
  ```

public class Athlete {
  static String raceLocation = "New York";
  static String raceStartTime = "9.00am";

  String name;
  int speed;
  int bibNumber;
  
  Athlete (String name, int speed){
      this.name = name;
      this.speed = speed;
  }

  static double calculateDuration(double startSec, double finishSec){ // code }

  void run(){ // code }
}
    
```
  The static member variables in the Athlete class can be a accessed and modified without an object/instance of Athlete.
  This does not work for non-static member variables:
  ```

Athlete.raceLocation = "NYC";           // OK!
Athlete.name = "Jim";                   // ERROR!

Athlete jim = new Athlete("Jim", 10);   // Athlete object/instance jim

jim.raceLocation = "Boston";            // OK!
jim.name = "Jimmy"                      // OK!
    
```
  ### 2. Only 1 Static Variable for all Objects of a Class
  There is only 1 static member variable for all objects of a class.
  There are unique variables for each object of a class. For example:
  ```

Athlete jim = new Athlete("Jim", 10);
Athlete amy = new Athlete("Amy", 6);

System.out.println(jim.name);           // prints "Jim"
System.out.println(amy.name);           // prints "Amy"
System.out.println(jim.raceStartTime);  // prints "9.00am"
System.out.println(amy.raceStartTime);  // prints "9.00am"

```
  In this example changing raceStartTime for jim to "10.00am" also changes the raceStartTime for amy.
  The raceStartTime variable is the same for both jim and amy.
  ### 3. Non-Static Member Variables and Methods can not be put inside Static Methods
  static methods can also be called before an object of a class exists, while non-static methods can't:
  ```

Athlete.calculateDuration(0.0, 14.7);   // OK!
Athlete.run();                          // ERROR!
Athlete jim = new Athlete("Jim", 10);
jim.run();                              // OK!
jim.calculateDuration(0.0, 14.7);       // OK!
    
```
  This is why non-static member variables and methods can't be placed inside of static methods.
  Static methods can be called before an object is created when non-static member variables haven't been created yet!
  ```

static double calculateDuration(double startSec, double finishSec){
    double durationSec = finishSec - startSec;
    
    System.out.println(name + " ran the race in " + durationSec + " seconds."); // ERROR! name is non-static
    return durationSec;
}

```
  The
  <b>
   this
  </b>
  keyword refers to an object so it can't be put inside of a static method either:
  ```

public static void main(String[] args){
    JFrame frame = new JFrame();
    frame.addActionListener(this);      // ERROR!
}

```
 </div>

