# 04 Gui From Scratch 2 Jack In The Box


 <div id="moduleIndex">
  # Jack-in-the-Box
  1. Create a user interface (GUI) that has a single button labeled "Surprise".
      If you need help, take a look at the instructions for the Fortune Cookie recipe.
  2. When the user presses the button 5 times, show them a jack-in-the-box using the methods below.
     (A sample jackInTheBox.png file is provided in the default package)
  private void showPicture(String fileName) { 
     try {

          JLabel imageLabel = createLabelImage(fileName);
          JFrame frame = new JFrame();
          frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
          frame.add(imageLabel);
          frame.setVisible(true);
          frame.pack();
     } catch (Exception e) {
          e.printStackTrace();
     }
}
  private JLabel createLabelImage(String fileName) {
	     try {			
	          URL imageURL = getClass().getResource(fileName);
	          if (imageURL == null) {
	               System.err.println("Could not find image " + fileName);
	               return new JLabel();
          } else {
               Icon icon = new ImageIcon(imageURL);
               JLabel imageLabel = new JLabel(icon);
               return imageLabel;
             }  
     } catch (Exception e) {
          System.err.println("Could not find image " + fileName);
          return new JLabel();
         }
}
  3. Also play a sound when the jack-in-the-box pops up using this method.
        (A sample sound homer-woohoo.wav is provided in the default package)

    private void playSound(String soundFile) { 
     try {
          AudioClip sound = JApplet.newAudioClip(getClass().getResource(soundFile));
          sound.play();
     } catch (Exception e) {
          e.printStackTrace();
     }
}
 </div>

