# 11 Binary Converter


 <div id="moduleIndex">
  # Flappy Bird
  1. Start a new sketch with draw and setup methods.

2. Set your canvas size in the setup method
  size(width, height)
  3. In your draw method, set a background, and draw a ball (bird) on the screen.
  ```
background(red, green, blue);
fill(red, green, blue);
stroke(red, green, blue);
ellipse(x, y, width, height);

```
  4. Make the bird fall down
         Hint: make variables for the bird's X and Y position and use them for the ellipse in the draw method.
  5. Add velocity to the bird. 
         Hint: make a variable for the velocity of the bird in the Y direction (up). Changing its value should change the velocity of your bird.
  int birdYVelocity = -10;
  6.  Give the bird gravity.
         Hint: make a variable for the gravity pulling the bird down. Gravity should continually increase the value of birdYVelocity.
  int gravity = 1;
  7. Make the bird jump (flap) when the mouse is clicked.
          Hint: construct a mousePressed() method the same way setup() and draw() were made. 
         In this method, reset the bird’s velocity to make the bird rise.
  8.  Draw a pipe coming down from the top of the sketch.

      In the draw() method:
  fill(red, green, blue);
rect(x, y, width, height);
  9. Make the pipe move from right to left.

     Hint: make a variable for the pipe X position and change it in the draw method.
  10. Make the pipe teleport back to the right side of the screen once it has passed through the left. This will simulate the repeating pipes coming from the right of the screen.
      Tip: Put this code into a teleportPipes() method and you can also call it from the setup() method to create the first pipes.
  11. Set the upper pipe's height to a new random number each time it teleports
  int upperPipeHeight = (int) random(100, 400);
  12. Create a variable, pipeGap, to represent the gap between the pipes. Make sure the gap is big enough for the ball to go through. The gap between the pipes will not change.
  13. Make a second pipe that will go down to the bottom of the sketch, leaving a space between the two pipes that is the size of the gap (see step 12). Make sure both pipes use the same value for their x position. Set the lower pipe y value by adding the upper pipe height and pipe gap. Ex:
  lowerY = upperPipeHeight + pipeGap;
  14. Make the game end when the bird hits the pipe. Figure it out by yourself, or use this method:
  ```
boolean intersectsPipes() { 
         if (birdY &lt; upperPipeHeight &amp;&amp; birdX &gt; pipeX &amp;&amp; birdX &lt; (pipeX+pipeWidth)){
            return true; }
        else if (birdY&gt;lowerPipeTop &amp;&amp; birdX &gt; pipeX &amp;&amp; birdX &lt; (pipeX+pipeWidth)) {
            return true; }
        else { return false; }
}
```
  15. End the game when the bird hits the ground.
     Make a rectangle for the ground.
     Use a boolean variable at the top of the sketch to indicate if game has ended.
  17.  Create a score and make it increase each time the bird passes through a pipe.
  text(text, xPosition, yPosition);
  18. OPTIONAL.   Use images for the background, pipes and bird (see image at top). You can find your own images, or those provided in the Module 3 Java project. See below for code snippets to load and draw images.


PImage back;
PImage pipeBottom;
PImage pipeTop;
PImage bird;
   void setup() {
       back = loadImage("flappyBackground.jpg");
       pipeBottom = loadImage("bottomPipe.png");
       pipeTop = loadImage("topPipe.png");
       bird = loadImage("bird.png");
       bird.resize(50,50);
   }
   void draw() {
       background(back);
       image (pipeBottom,250,375);
       image (pipeTop,250,-130);
       image (bird, 250, 300);
   }
 </div>

