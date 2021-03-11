# Python code to convert an image to ASCII image. 
# importing all the libraries we need
import sys, random, argparse, math, os
import numpy as np 
from PIL import Image
import zipfile38 as zipfile
print("end file path with a / otherwise the program will crash")
print("if you run into issues, refer to github/issue or read the README.txt included")
print("Also you will need folders PNG_15 for LOWQ(128x96)")
print("PNG_30 For ASCII (94x70) and SCAN(94x70)")
print("and PNG_60 for HQ versions.")
print("Assuming these folders exist, you can run this file, or CTRL+C to exit it now.\n")
print("Also store the image source folders in the parent folder /BADAPPLE/ otherwise, Crash.\n")
pathtofiles = input("specify BADAPPLE folders location(example. C:/BADAPPLE/ or D:/some/folders/BADAPPLE/): ")
buff_pathtofiles = pathtofiles

try:
    os.makedirs(pathtofiles + str("ASCII/"))
except:
    print("Folder ASCII Exists, skipping")
try:
    os.makedirs(pathtofiles + str("ASCII_HQ/"))
except:
    print("Folder ASCII_HQ Exists, skipping")
try:
    os.makedirs(pathtofiles + str("LOWQ/"))
except:
    print("Folder LOWQ Exists, skipping")
try:
    os.makedirs(pathtofiles + str("SCAN/"))
except:
    print("Folder SCAN Exists, skipping")

#checks for png files

if os.path.isdir(pathtofiles) == True:
    print("Parent Folder Exists")

elif os.path.isdir(pathtofiles) == False:
    print("Parent Folder is the wrong name or missing, try again")
    sys.exit()

if os.path.isdir(pathtofiles + str("PNG_15/")) == True:
    print("PNG_15 Folder Exists")
    
elif os.path.isfile(pathtofiles + str("PNG_15/")) == False:
    print("PNG_15 Doesn't exist,extract the files to /BADAPPLE/ and try again")
    sys.exit()
    
if os.path.isdir(pathtofiles + str("PNG_30/")) == True:
    print("PNG_30 Exists")
    
elif os.path.isdir(pathtofiles + str("PNG_30/")) == False:
    print("PNG_30 Doesn't exist, extract the files to /BADAPPLE/ and try again")
    sys.exit()
    
if os.path.isdir(pathtofiles + str("PNG_60/")) == True:
    print("PNG_60 Exists")
    
elif os.path.isdir(pathtofiles + str("PNG_60/")) == False:
    print("PNG_60 Doesn't exist, extract the files to /BADAPPLE/ and try again")
    sys.exit()
    
# gray scale level values from:  
# http://paulbourke.net/dataformats/asciiart/ 

# 70 levels of gray 
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
  
# 10 levels of gray 
gscale2 = '#####     '
  
def getAverageL(image): 
  
    """ 
    Given PIL Image, return average value of grayscale value 
    """
    # get image as numpy array 
    im = np.array(image) 
  
    # get shape 
    w,h = im.shape 
  
    # get average 
    return np.average(im.reshape(w*h)) 
  
def covertImageToAscii(fileName, cols, scale, moreLevels):
    fileName = PNG_Source + str(filenum)
    fileName = fileName + ".png"
    cols = int(usr_width)
    scale = 1
    moreLevels = int(detail)
    """ 
    Given Image and dims (rows, cols) returns an m*n list of Images  
    """
    # declare globals 
    global gscale1, gscale2 
  
    # open image and convert to grayscale 
    image = Image.open(fileName).convert('L') 
  
    # store dimensions 
    W, H = image.size[0], image.size[1] 
    print("input image dims: %d x %d" % (W, H)) 
  
    # compute width of tile 
    w = W/cols 
  
    # compute tile height based on aspect ratio and scale 
    h = w/scale 
  
    # compute number of rows 
    rows = int(usr_height)
      
    print("cols: %d, rows: %d" % (cols, rows)) 
    print("tile dims: %d x %d" % (w, h)) 
  
    # check if image size is too small 
    if cols > W or rows > H: 
        print("Image too small for specified cols!") 
        exit() 
  
    # ascii image is a list of character strings 
    aimg = [] 
    # generate list of dimensions 
    for j in range(rows): 
        y1 = int(j*h) 
        y2 = int((j+1)*h) 
  
        # correct last tile 
        if j == rows-1: 
            y2 = H 
  
        # append an empty string 
        aimg.append("") 
  
        for i in range(cols): 
  
            # crop image to tile 
            x1 = int(i*w) 
            x2 = int((i+1)*w) 
  
            # correct last tile 
            if i == cols-1: 
                x2 = W 
  
            # crop image to extract tile 
            img = image.crop((x1, y1, x2, y2)) 
  
            # get average luminance 
            avg = int(getAverageL(img)) 
  
            # look up ascii char 
            if moreLevels: 
                gsval = gscale1[int((avg*69)/255)] 
            else: 
                gsval = gscale2[int((avg*int(amount))/255)] 
  
            # append ascii char to string 
            aimg[j] += gsval 
      
    # return txt image 
    return aimg 
  
# main() function 
def main(): 
    # create parser 
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr) 
    # add expected arguments 
    parser.add_argument('--file', dest='imgFile', required=False) 
    parser.add_argument('--scale', dest='scale', required=False) 
    parser.add_argument('--out', dest='outFile', required=False) 
    parser.add_argument('--cols', dest='cols', required=False) 
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true') 
  
    # parse args 
    args = parser.parse_args() 
    
    imgFile = args.imgFile 
  
    # set output file 
    outFile = directory + str(filenum)
    outFile = outFile + ".txt"
    if args.outFile: 
        outFile = args.outFile 
  
    # set scale default as 0.43 which suits 
    # a Courier font 
    scale = 0.43
    if args.scale: 
        scale = float(args.scale) 
  
    # set cols 
    cols = 64
    if args.cols: 
        cols = int(args.cols) 
  
    print('generating ASCII art...') 
    # convert image to ascii txt 
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels) 
  
    # open file 
    f = open(outFile, 'w', encoding="utf-8")
  
    # write to file 
    for row in aimg: 
        f.write(row + '\n') 
  
    # cleanup 
    f.close() 
    print("ASCII art written to %s" % outFile) 
  
# Load relevant values
filenum = 1
# set resolution
usr_width = int(94)
usr_height = int(70)
# call gscale2
detail = 0
gscale2 = '#####     '
amount = 9
# call files
directory = pathtofiles
PNG_Source = pathtofiles + str ("PNG_30/")
directory = directory + str("ASCII/")
# call main()
for i in range(6571):
    str(filenum)
    main()
    filenum +=1
# load values for ASCII_HQ
filenum = 1
# set resolution
usr_width = int(120)
usr_height = int(90)
# call gscale1
detail = 1
# call files
directory = pathtofiles
PNG_Source = pathtofiles + str ("PNG_60/")
directory = directory + str("ASCII_HQ/")
for i in range(13141):
    str(filenum)
    main()
    filenum +=1

filenum = 1
# set resolution
usr_width = int(94)
usr_height = int(70)
# call gscale1
detail = 0
gscale2 = '_____     '
amount = 9
# call files
directory = pathtofiles
PNG_Source = pathtofiles + str ("PNG_30/")
directory = directory + str("SCAN/")
for i in range(6571):
    str(filenum)
    main()
    filenum +=1

filenum = 1
# set resolution
usr_width = int(60)
usr_height = int(45)
# call gscale1
detail = 0
gscale2 = '█▓▒░  '
amount = 5
# call files
directory = pathtofiles
PNG_Source = pathtofiles + str ("PNG_15/")
directory = directory + str("LOWQ/")
for i in range(3285):
    str(filenum)
    main()
    filenum +=1
