import time

filenum = 1

input()
print(" ####\n"*59)
input()

for i in range(25):
    directory = "G:/BADAPPLE/ASCII/" +  str(filenum)
    file = open(directory + ".txt","r")
    data = file.read()
    print(data)
    filenum += 1
    time.sleep(0.03333333)
