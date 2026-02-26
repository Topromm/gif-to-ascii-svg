# GIF/Video → Animated ASCII SVG (GitHub‑Friendly)
<img src="animation.svg">

I created this project to showcase how you can turn any video into a fully animated SVG made entirely out of ASCII art.  
The final SVG plays directly inside GitHub's README without JavaScript, images, or external hosting. You just need to have Python installed.

Below is the full process so anyone can recreate it.

---

## 1. Start with any video
Pick a short clip. High contrast works best for ASCII.

---

## 2. Convert the video to a GIF
Use this tool: https://ezgif.com/video-to-gif

This gives you a frame‑by‑frame animation that ASCII tools can process.

---

## 3. Create a URL for the GIF
The next tool we will be using will need the GIF in a URL format to convert it to ASCII art.
Personally, I uploaded my GIF to Giphy, I make it fast and easy using a tool like [ShareX](https://getsharex.com/)

In a pinch, you could also share the GIF to yourself on Discord, and copy the GIF link from there.

---

## 4. Convert the GIF into ASCII frames
Use: https://asciigif.com/ (shoutout to [JayRichh](https://github.com/JayRichh/ascii) for creating the website)

Choose "ASCII text" as the output format

This gives you a `.txt` file, save it as `frames.txt`. 

Now you should count the number of lines each "frame" has to get it's height, as well as the number of characters per line to get it's width.

In my case:
- Each frame was 91 lines tall
- Each line was 91 characters wide
- Frames are separated by one blank line

You should add your line height, character width and any other preferred values at the top of svg_build.py and svg_build_clean.py

---

## 5. build the SVG animation
Run svg_build.py to create your own animation.svg that you can insert into your README.

---

## 6. (Optional) Clean the ASCII file
ASCII files often contain heavy characters like @ and % that dominate the background of the image.
I've included an svg_cleaner.py that removes every @ and % from ALL frames of the animation.
You can edit said svg_cleaner.py to remove or replace whatever characters you want.
This will create a separate copy of your frames called frames_clean.txt
Then run svg_build_clean.py to create your own animation.svg

---

## License
© Copyright 2026 Topromm. All rights reserved.
