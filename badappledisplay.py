import time


Start = time.time()

filenum = 1

input()
print("\n"*100)
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

Start = time.time()

import fpstimer
timer = fpstimer.FPSTimer(30) # Make a timer that is set for 60 fps.
for i in range(6572): # Each iteration of this loop will last (at least) 1/60 of a second.
    # Do calculations/work for a single "frame" here.
    directory = "G:/BADAPPLE/ASCII/" +  str(filenum)
    file = open(directory + ".txt","r")
    data = file.read()
    print(data)
    filenum += 1
    timer.sleep() # Pause just enough to have a 1/60 second wait since last fpstSleep() call.

end = time.time()

Time = end - Start

print(Time)
		
		
		
		
