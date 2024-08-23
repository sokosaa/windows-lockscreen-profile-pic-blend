0. `pip install pillow`
1. set `images/black_pixel.png` as your microsoft profile picture
2. set `images/6016_whiterow.jpg` as your lock screen background
3. edit `edit.py` until the top and bottom of the profile picture ont he lock scren ar just barely touching (just barely no white or gray space) or maybe actually you want some gray?
4. run `crop_and_darken.py` on `gray.jpg` with one pixel lower and one pixel higher than you used in your final `edit.py` run
5. mess with brightness in `crop_and_darken.py` untill it blends in all the way for `gray.jpg`
6. switch to your main image in `crop_and_darken.py` and run it, there you have your profile picture
