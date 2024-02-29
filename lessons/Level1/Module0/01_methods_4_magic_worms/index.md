# 01 Methods 4 Magic Worms


 <div id="moduleIndex">
  # Magic Worms
  1. Start a new sketch with draw, setup, and settings methods.

2. Set your canvas size and background color in the settings() method
  ```
    size(width, height
    background(red, green, blue)
```
  3. In your draw method, use a for loop to draw 300 ellipses in a diagonal line across the canvas.
    RUN THE PROGRAM TO CHECK IT.
  4. Now change the x and y location of each ellipse to "different" random numbers that are inside the canvas. Note: random() returns values that are type float so your x and y variable types should also be float.
    RUN THE PROGRAM TO CHECK IT.
  ```
   random(int maxValue)
```
  5. Set the color of each ellipse.
    RUN THE PROGRAM TO CHECK IT.
  ```
    fill(red, green, blue)
```
  6.  If this code isn't already in your file, paste this code at the bottom.
  ```
    float frequency = .001;
    float noiseInterval = PI;

    void makeMagical() {
        fill( 0, 0, 0, 10 );
        rect(0, 0, width, height);
        noStroke();
    }

    float getWormX(int i) {
        return map(noise(i*noiseInterval + frameCount * frequency), 0, 1, 0, width);
    }

    float getWormY(int i) {
        return map(noise(i*noiseInterval+1 + frameCount * frequency), 0, 1, 0, height);
    }
```
  7. Now change the x and y location of each ellipse to the value returned by the getWormX() and getWormY() methods (use the for loop variable as the parameter to these methods). 
    RUN THE PROGRAM TO CHECK IT.
  8. Call makeMagical() in your draw method before the for loop.  OPTIONS: Pass in frameCount or another variable for the ellipse "red value", and i as the "green value" for some extra color coolness.
    RUN THE PROGRAM TO CHECK IT.
  10. You can adjust the frequency and noiseInterval variables to your liking. Also play with the number and size of particles (ellipses) until it looks amazing.
  11. [Optional] Add another worm every time the user clicks the mouse.
 </div>

