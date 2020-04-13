# This is a clock hardcoded in python

import time
from os import system, name

print('Clock Started: ')
clock = [00, 00, 00]

# clock[0] = hours
# clock[1] = minutes
# clock[2] = seconds


while True:
    time.sleep(1)
    if name == 'nt':
        _ = system('cls')
    clock[2] += 1
    if clock[2] == 60:
        clock[2] = 0
        clock[1] += 1
    if clock[1] == 60:
        clock[1] = 0
        clock[0] +=1
    
    print(clock)
