import time, fpstimer, os, pathlib
from playsound import playsound

# get path to files 
filepath = pathlib.Path(__file__).parent.absolute()
truefilepath = str(filepath) + str("\\")
###########

def run():
    Start = time.time()
    filenum = 1
    timer = fpstimer.FPSTimer(float(fps)) 
    for i in range(files):
        directory = init_directory
        directory = directory + str(filenum)
        file = open(directory + ".txt","r", encoding="utf-8")
        data = file.read()
        print(data)
        filenum += 1
        timer.sleep() # Pause just enough to have a 1/60 second wait since last fpstSleep() call.

    end = time.time()

    Time = end - Start
    print("""
    thank you
    for watching
    untill the
    end.
    love, dev :)
    """)
    print(Time)
    time.sleep(1000)

def menu():
    global ver
    print("Choose The Number")
    ver = input("1. Original 2. Scanline 3. SNES 4. ASCII HQ 5.LOWQ 6. Widescreen: ")
    print("Are you sure you want to run option ", ver, "?(Y/N)")
    conf = input()

    while conf == "N":
        ver = input("1. Original 2. Scanline 3. SNES 4. ASCII 60 FPS 5.LOWQ 6. Widescreen: ")
        print("Are you sure you want to run option ", ver, "?(Y/N)")
        conf = input()
    global fps
    global files
    global init_directory
    if ver == "1":
        init_directory = "G:/BADAPPLE/ASCII/"
        fps = int(30)
        files = int(6571)
    elif ver == "2":
        init_directory = "G:/BADAPPLE/SCAN/"
        fps = int(30)
        files = int(6571)
    elif ver == "3":
        init_directory = str(truefilepath) + "SNES\\"
        fps = int(10)
        files = int(2191)
    elif ver == "4":
        init_directory = str(truefilepath) + "ASCII_HQ\\"
        fps = int(60)
        files = int(13141)
    elif ver == "5":
        init_directory = str(truefilepath) + "LOWQ\\"
        fps = int(60)
        files = int(13141)
    elif ver == "6":
        init_directory = str(truefilepath) + "WIDESCREEN\\"
        fps = int(60)
        files = int(13166)
        
    input()
    print("\n"*1000)
    input()

#LEGACY

###########################################################

#Start = time.time()

#for i in range(6572):
    #directory = "G:/BADAPPLE/ASCII/" +  str(filenum)
    #file = open(directory + ".txt","r")
    #data = file.read()
    #print(data)
    #filenum += 1
    #time.sleep(0.012685)
    
#end = time.time()

#Time = end - Start

#print(Time)

###########################################################
print("Reading files from:", truefilepath)

menu()
if ver == "1":
    os.system("mode con cols=94 lines=70")
    playsounddir = truefilepath + "BADAPPLE.wav"
    playsound(playsounddir, block = False)
elif ver == "5":
    os.system("mode con cols=120 lines=90")
    playsounddir = truefilepath + "BADAPPLE.wav"
    playsound(playsounddir, block = False)
    run()
elif ver == "3":
    os.system("mode con cols=32 lines=24")
    playsounddir = truefilepath + "BADAPPLE_SNES.mp3"
    playsound(playsounddir, block = False)
    run()
elif ver == "6":
    os.system("mode con cols=208 lines=117")
    playsounddir = truefilepath + "BADAPPLE.wav"
    playsound(playsounddir, block = False)
    run()

playsounddir = truefilepath + "BADAPPLE.wav"
playsound(playsounddir, block = False)
run()
