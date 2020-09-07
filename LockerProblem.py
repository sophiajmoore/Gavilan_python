# Locker Problem
# Sophia Moore
# 7/17/20
# Python 3.8.3

# Problem:
# There are 1000 locked lockers
# Student #1 opens all lockers
# Student #2 closes every other locker
# Student #3 opens/closes every third locker depending on if the locker is originally opened/closed
# This continues until Student #1000
# How many lockers are open at the end?

lockers = []

# all lockers set to locked
for i in range(0,1000,1): # locker 0 thru locker 999 -- 1000 lockers
    lockers.append(1) # add 1 to lockers 1000 times (1 = locked)

# first student opening all lockers
for i in range(0,1000,1): # last number means skip that amount
    if lockers[i] == 1: # if locker is locked
        lockers[i] = 0  # open it
    elif lockers[i] == 0: # if locker is open
        lockers[i] = 1  # lock it

# the rest of the students
for j in range(2,1001,1): # from 3 to 1000
    for i in range(0,1000,j): # last number means skip that amount
        if lockers[i] == 1: # if locker is locked
            lockers[i] = 0  # open it
        elif lockers[i] == 0: # if locker is open
            lockers[i] = 1  # lock it


# printing which lockers are open
for i in range(0,1000,1):
    if lockers[i] == 0: # if locker is open
        print('Locker %i is open' %i) # print it

# printing the number of lockers open
Sum = 0
for i in range(0,1000,1):
    if lockers[i] == 0:
        Sum += 1
print("There are %i lockers open!" %Sum)

'''
=========== RESTART: /Users/sophiajmoore/Desktop/class/p26Lockers.py ===========
Locker 1 is open
Locker 4 is open
Locker 9 is open
Locker 16 is open
Locker 25 is open
Locker 36 is open
Locker 49 is open
Locker 64 is open
Locker 81 is open
Locker 100 is open
Locker 121 is open
Locker 144 is open
Locker 169 is open
Locker 196 is open
Locker 225 is open
Locker 256 is open
Locker 289 is open
Locker 324 is open
Locker 361 is open
Locker 400 is open
Locker 441 is open
Locker 484 is open
Locker 529 is open
Locker 576 is open
Locker 625 is open
Locker 676 is open
Locker 729 is open
Locker 784 is open
Locker 841 is open
Locker 900 is open
Locker 961 is open
There are 31 lockers open!
>>>
'''
