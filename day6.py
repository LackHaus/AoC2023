# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:58:11 2023

@author: tholac1
"""
import numpy as np

pt_2 = True


f = open("day6.txt", "r")

times = []
distances = []

data = f.readlines()

for c,v in enumerate(data[0].split(" ")):
    if (v != "") and (":" not in v):
        times.append(int(v))
        
for c,v in enumerate(data[1].split(" ")):
    if (v != "") and (":" not in v):
        distances.append(int(v))

if not pt_2:
    
        

    mul_of_ways = 1
    for c,race_time in enumerate(times):
        ways = 0
        for btn_held in range(0, race_time+1):
            if (race_time-btn_held)*btn_held > distances[c]:
                ways += 1
        mul_of_ways = mul_of_ways*ways
    print(mul_of_ways)
    
else:
    times_str = ""
    distances_str = ""
    for i in times:
        times_str = times_str + str(i)
    for i in distances:
        distances_str = distances_str + str(i)
    time = int(times_str)
    distance = int(distances_str)
    start = 0
    end = 0
    for i in range(0, time+1):
        if (time-i)*i > distance:
            start = i
            break
    for i in reversed(range(0, time+1)):
        if (time-i)*i > distance:
            end = i
            break
    print(end-start+1)
        

                
    
