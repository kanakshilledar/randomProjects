# This is a curTime hardcoded in python
# Just using a few libraries
# Program Written By Kanak Shilledar

# importing libraries
import datetime
import time
from os import system, name

# converting the datetime datatype to list
curTime = datetime.datetime.now()
curTime = str(curTime)
curTime = curTime[11:19]
curTime = list(curTime)
for ele in range(len(curTime) - 2):
    if curTime[ele] == ':':
        curTime.pop(ele)
    
for ele in range(0, len(curTime) - 1):
    curTime[ele] = curTime[ele] + curTime[ele + 1]
for i in range(1, 4):
    curTime.pop(i)
for i in range(len(curTime)):
    curTime[i] = int(curTime[i])

# adding one sec to reduce the time lost
curTime[2] += 1
# initializing the curTime
print('Clock Started: ')

# curTime[0] = hours
# curTime[1] = minutes
# curTime[2] = seconds

# main algorithm
while True:
    time.sleep(1) # waiting for one second
    # clearing the screen
    if name == 'nt':
        _ = system('cls')
    curTime[2] += 1
    # for minute
    if curTime[2] == 60:
        curTime[2] = 0
        curTime[1] += 1
    # for hour
    if curTime[1] == 60:
        curTime[1] = 0
        curTime[0] +=1
    
    # printing the curTime
    print(curTime)
