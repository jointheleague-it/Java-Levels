# 04 Gui From Scratch 3 Sound Effects Machine


 <div id="moduleIndex">
  # Sound Effects Machine
  1.  Create a GUI for a sound effects machine that will play different sounds when the buttons are pressed.
      If you need help, take a look at the instructions for the Fortune Cookie recipe. 

     NOTE: because this GUI has more than one button, you must add a JPanel to your JFrame and put the buttons on the panel!

        2. Gather sound bites. They must be .wav files. Free sound effects can be found here. The League also has an account at freesound. Ask your teacher for our login.
        The .wav files must be placed into your recipe package(_3_sound_effects_machine) (drag and drop).

3. Call this playSound() method when they click on a button. You will need to import java.applet.AudioClip
  ```

	private void playSound(String soundFile) {
		String path = "src/_03_gui_from_scratch/_3_sound_effects_machine/";
			File sound = new File(path+soundFile);
			if (sound.exists()) {
				new Thread(() -&gt; {
				try {
					Clip clip = AudioSystem.getClip();
					clip.open(AudioSystem.getAudioInputStream(sound));
					clip.start();
					Thread.sleep(clip.getMicrosecondLength()/1000);
				}
				catch (Exception e) {
					System.out.println("Could not play this sound");
				}}).start();
	 		}
			else {
				System.out.println("File does not exist");
			}
		
	}
    
```
 </div>

