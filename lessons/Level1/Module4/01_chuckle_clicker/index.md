# 01 Chuckle Clicker


 <div id="moduleIndex">
  # Chuckle Clicker
  We are going to tell the user jokes that have punchlines.
  1. Make a ChuckleClicker class with a main method and a makeButtons() method. 
     Open a pop-up that shows the message "Make Buttons" in the makeButtons method, to prove that it is working.
     (You will need to instantiate your class before you can call the method). 


2. Now change the makeButtons() method, to make a JFrame and get it to show.


     3.Add a JPanel and two JButtons to the frame, so it looks a lot like this:




4. *[Optional] Customize your GUI with setText, setSize, etc.
  5. Make a pop-up that says “hi” when either of the buttons are pressed. You will need to add listeners to the buttons for this to work.

    6. Check if the ActionEvent came from the joke button or the punchline button.
  if(event.getSource() == jokeButton)
  Hint: You might need to move the declaration of your buttons outside of the makeButtons() method.
  7. Use JOptionPane to print the joke or the punchline depending on which button was clicked.
 </div>

