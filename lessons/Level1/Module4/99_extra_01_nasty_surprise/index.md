# 99 Extra 01 Nasty Surprise


 <div id="moduleIndex">
  # Nasty Surprise
  1. Make a user interface that has 2 buttons. One says “Trick” the other says “Treat”. 

2. When the user clicks on the Trick button, show them a picture of a cute puppy. 

3. When they click Treat, show them a scary image.

To show the pictures, use the showPictureFromTheInternet() method below.
  ```
private void showPictureFromTheInternet(String imageUrl) {
    try {
        URL url = new URL(imageUrl);
        Icon icon = new ImageIcon(url);
        JLabel imageLabel = new JLabel(icon);
        JFrame frame = new JFrame();
        frame.add(imageLabel);
        frame.setVisible(true);
        frame.pack();
    } catch (MalformedURLException e) {
        e.printStackTrace();
    }
}
```
 </div>

