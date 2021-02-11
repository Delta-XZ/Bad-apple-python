This file will show you how to re create [YT video link]

Required applications:

ffmpeg

python IDE (i used the default python IDLE)

Rouhly 200 MB of free space

Step 1.

splice the video to frames in ffmpeg using:
ffmpeg -i input.mp4 -vf fps=30/1 out%d.png

where input.mp4 can be any video file as in input.flv or myvid.mp4, as long as ffmpeg supports it

30/1 is just frames/second so 1/30 would take a frame every 30 seconds. we will be using 30 fps as the video is natively 30 fps

out%d.png is your output file where "out" can be anything, i left it blank. also you can change from png to the format of your desire, although jpg bugged out for me
so i got duped frames, use png to be safe

i recommend saving the files to a "master folder", my file path was G:/BADAPPLE/JPG/ for images and G:/BADAPPLE/ASCII/ for the txt files.
so my config would be ffmpeg -i C:/Users/[username]/Downloads/BADAPPLE.mp4 -vf fps=30/1 %d.png


Step 2.

now that we have the images, we need to convert them to ascii. im not going in detail now,
but most likely will give an in depth look at the code.

convert images to ascii using ascii.py

change file paths to be appropriate
or use the values i provided in ascii.py
dont touch filenum as it allows us to save the files without overwriting

only touch the quoted areas in fileName at lines 33 and 34
the cols and scale are setup to take up the IDLE window (Width = 118, Height = 59)

step 3.

using badappledisplay.py, we can read these text files and print them to the console.
time.sleep should be 0.014999... to get the program to run exactly 219 seconds (Length of the original video)

step 4.

run in python IDLE
i wrote this in 3.9.1 so it might break in the future

sources:
python IDLE: python.org
ascii.py source code: https://www.geeksforgeeks.org/converting-image-ascii-image-python/
ffmpeg: ffmpeg.org/
