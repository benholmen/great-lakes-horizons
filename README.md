# Great Lakes Horizons Project

I've been taking photos of Great Lakes horizons (mostly Superior, to be honest) in an effort to document and record the light and weather conditions from hour to hour. My intention is to create a large gallery - physical or digital - of the great lake, the sky, and the huge variety of conditions that you find on the lakes.

## What this code does

I'd like to automate the rotation and cropping of the original photos. They are all within a few degrees of a nominal horizon, and have similar crops, but I want them to be exactly the same. This code is experimental and a learning experience.

### First attempt - Algorithmia

I first tried using Algorithmia as documented [here](https://blog.algorithmia.com/how-to-rotate-images-in-python-using-a-horizon-detection-algorithm). I found that it did not reliably detect the horizon with enough accuracy. It might work for you and it's free for hobby use because they give a generous number of monthly credits.

### Second attempt - cv2 Canny/HoughLinesP

This seems much more accurate for the types of images I am using.
