import time

#uncomment time.time lines for time monitoring(seconds)
#Start = time.time()

filenum = 1
#clears the screen
input()
print("\n"*61)
input()

for i in range(6572):
    #directory = disk/folder/folder/
    #change to suit your system
    directory = "G:/BADAPPLE/ASCII/" +  str(filenum)
    file = open(directory + ".txt","r")
    data = file.read()
    print(data)
    filenum += 1
    time.sleep(0.0149999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

#end = time.time()

#Time = end - Start

#print(Time)
