# Reading and writing to a file
# Sophia Moore
# 7/23/20
# Python 3.8.3
# Description: a program that cutes and prints the average for each year

myFile = open("inputdata.txt", "r")
fileAsListOfLines = myFile.read().splitlines()
myFile.close()

otherFile = open("outputdata.txt", "w")
otherFile.write("year   average\n")
for j in range(0,len(fileAsListOfLines),1):
    aLine = fileAsListOfLines[j]
    lineData = aLine.split()
    year = lineData[0] # the year is the first thing in the list
    sumData = 0
    for i in range(1,len(lineData),1):
        sumData += float(lineData[i])
    avg = sumData/(len(lineData)-1)
    otherFile.write("%s   %.2f \n" %(year,avg))

otherFile.close()
