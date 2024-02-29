# 01 Methods 3 Rain Game


 <div id="moduleIndex">
  # Rain Game
  1. Start a new sketch with draw, setup, and settings methods.

2. Set your canvas size in the settings() method
  ```
    size(width, height)
```
  and your background color in the draw method
  ```
    background(red, green, blue)
```
  3. Draw a raindrop at the top of the screen in the draw() method.
  ```

    fill(red, green, blue);
    stroke(red, green, blue);
    ellipse(x, y, width, height);
```
  4. Make the rain fall down the screen.
         Hint: make a variable for the raindrop's Y position and change it in the draw method.
  5. When the rain falls off the bottom of the canvas, start a new rain drop falling from the top.
  6.  Make the rain start at a random position (X position) at the top. This code will give you a random number between 0 and the width of your sketch.
  ```
      int randomNumber = (int) random(width);
```
  7. Draw a bucket at the bottom of the screen.
  ```
        rect(int x, int y, int width, int height);
```
  8. Make the bucket move over and back with the mouse. Hint: mouseX
  9. Add an int variable to hold the score (above the setup method). If the rain falls in the bucket increase the score by 1. If it doesn’t, decrease the score by 1, but don’t let the score go negative. Figure it out by yourself or use this method…

    void checkCatch(int x){
         if (x &gt; mouseX &amp;&amp; x &lt; mouseX+100)
            score++;
         else if (score &gt; 0) 
            score--;
        println("Your score is now: " + score);
    }

  10. Print the score on the screen.

    fill(0, 0, 0);
    textSize(16);
    text("Score: " + score, 20, 20);
 </div>

