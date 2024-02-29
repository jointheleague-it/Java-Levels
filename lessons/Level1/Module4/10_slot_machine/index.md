# 10 Slot Machine


 <div id="moduleIndex">
  # Slot Machine
  We are going to make a slot machine.
  The slot machine we are going to make, will look a little like the middle row on this image:
  First, find 3 images for the slot machine to display, e.g. cherry, orange, lime.

            Each "reel" of the slot machine will randomly display one of 3 images you have chosen (you can add more images later if there is time).



    Put a "SPIN" button onto the frame that causes each of the 3 "reels" to randomly change the image they are showing.


    If all 3 reels have the same image showing (like in the picture above), the player wins. Display a "YOU WIN" message, optionally add a sound of success, and if you are still having fun - update a win counter to show the user how many times they have won.


    You may find the code below helpful:


private JLabel createLabelImage(String fileName) throws MalformedURLException{
        URL imageURL = getClass().getResource(fileName);
	if (imageURL == null){
		System.err.println("Could not find image " + fileName);
		return new JLabel();
	}
	Icon icon = new ImageIcon(imageURL);
	JLabel imageLabel = new JLabel(icon);
	return imageLabel;
}
 </div>

