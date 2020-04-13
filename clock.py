# This is a clock hardcoded in python
# Just using a few libraries
# Program Written By Kanak Shilledar

# importing libraries
import time
from os import system, name

# initializing the clock
print('Clock Started: ')
clock = [00, 00, 00]

# clock[0] = hours
# clock[1] = minutes
# clock[2] = seconds

# main algorithm
while True:
    time.sleep(1) # waiting for one second
    # clearing the screen
    if name == 'nt':
        _ = system('cls')
    clock[2] += 1
    # for minute
    if clock[2] == 60:
        clock[2] = 0
        clock[1] += 1
    # for hour
    if clock[1] == 60:
        clock[1] = 0
        clock[0] +=1
    
    # printing the clock
    print(clock)
