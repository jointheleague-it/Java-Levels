# 04 Gui From Scratch 1 Fortune Cookie


 <div id="moduleIndex">
  # Fortune Cookie
  Goal: Make a Swing program from scratch.
The program will have a window (frame) with a button that gives one of five random fortunes when clicked.
  1. Make a FortuneCookie class, with a showButton() method like the one below: 

       public class FortuneCookie {
        public void showButton() {
            System.out.println("Button clicked");
       }
    }

    2. Now make a runner class to run the code above, like the one below: 

           public class FortuneCookieRunner {
        public static void main(String[] args) {
            new FortuneCookie().showButton();
      }
   }

    3. Now change the showButton() method in Step 1, to make a JFrame and get it to show up when you run the program. Hint:
   frame.setVisible(true);

    4. Make a JButton and add it to the JFrame.
    JButton button = new JButton();
    frame.add(button);
    frame.pack();

    5. The next 4 steps make a pop-up appear that says, “Woohoo” when the button is clicked

        a. Add an action listener to the button: 
button.addActionListener(this);

           b. Have your class implement ActionListener [use Eclipse quick fix]

           c. Add the unimplemented methods [use Eclipse quick fix]

           d. Put a JOptionPane pop-up inside the actionPerformed() method that says "Woohoo".

      6. Generate a random number between 0 and 4: 
   int rand = new Random().nextInt(5);
7. Depending on which random number, show one of the five fortunes.

[optional] 8. Run other student's programs to receive fortunes from them.
 </div>

