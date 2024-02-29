# 04 Gui From Scratch 4 Cuteness Tv


 <div id="moduleIndex">
  # Cuteness TV
  1. Make a user interface with 3 buttons that will play different videos depending on which button is clicked. 

      If you need help, take a look at the instructions for the Fortune Cookie recipe. 


  2.  Use the methods below to play the cutest videos ever.
  void showDucks() {
     playVideo("https://www.youtube.com/watch?v=MtN1YnoL46Q");
}

  void showFrog() {
     playVideo("https://www.youtube.com/watch?v=cBkWhkAZ9ds");
}

     void showFluffyUnicorns() {
     playVideo("https://www.youtube.com/watch?v=a-xWhG4UU_Y");
}

     void playVideo(String videoID) {
          
      // Workaround for Linux because "Desktop.getDesktop().browse()" doesn't 
      //work on some Linux implementations 
     try { 
     if (System.getProperty("os.name").toLowerCase().contains("linux")) {
     if (Runtime.getRuntime().exec(new String[] { 
      "which", "xdg- open" }).getInputStream().read() != -1) {
     Runtime.getRuntime().exec(new String[] { "xdg-open", videoID }); 

     }
     } else {


          URI uri = new URI(videoID);
          java.awt.Desktop.getDesktop().browse(uri);
     }
     } catch (Exception e) {
          e.printStackTrace();

     }
	}
  Note: If any of these video links no longer work, go to youtube and get replacements. Use the method names to give you a hint about what the videos should contain :)
 </div>

