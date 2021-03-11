import os
print("execute in same folder as videos")
input()
try:
    os.system("mkdir png_60")
except:
    print()    
try:
    os.system("mkdir png_30")
except:
    print()    
try:
    os.system("mkdir png_15")
except:
    print()    
try:
    os.system("mkdir png_10")
except:
    print()

os.system("ffmpeg -i badapple.mp4 -vf fps=30/1 png_30\%d.png")
os.system("ffmpeg -i badapple60.mp4 -vf fps=60/1 png_60\%d.png")
os.system("ffmpeg -i badapple.mp4 -s 128x96 -vf fps=15/1 png_15\%d.png")
os.system("ffmpeg -i badapple.mp4 -s 64x48 -vf fps=10/1 png_10\%d.png")
