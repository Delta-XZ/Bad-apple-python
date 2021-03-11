how to turn bad apple, or any other video, into ascii art that runs off of the python output


Step 1.

splice the badapple.mp4 file in ffmpeg with
ffmpeg -i input.mp4 -vf fps=30/1 out%d.png

where input.mp4 is disk:/directory/badapple.mp4
and out%d.png is disk:/badapple/png/%d.png

step 2.

convert png to ascii with ascii.py

change fileName and OutFile to change input and output.
this will turn the pngs into txt files.
recommended to output the txt files to a seperate folder (i used disk:/BADAPPLE/ASCII/)

step 3.

specify input folder to badappledisplay.py if needed and run.
works both with py.exe and idle.

if you run into issues feel free to open an issue.


sources:
python IDLE: python.org
ascii.py source code: https://www.geeksforgeeks.org/converting-image-ascii-image-python/
ffmpeg: ffmpeg.org/
