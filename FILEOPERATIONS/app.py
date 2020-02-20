import os

try:
    listOfNames = open("names2.txt", "x")
except:
    os.remove("names2.txt")
    listOfNames = open("names2.txt", "x")

#listOfNames.write("Larry Warry")
#listOfNames.close()

