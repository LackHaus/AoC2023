"""
LackHaus
Advent of code day 5!
"""

import numpy as np

pt_2 = True

f = open("day5.txt", "r")

data = f.readlines()

seeds = data[0].split(":")[1]
seeds = seeds.split(" ")[1:]

for c,v in enumerate(seeds):
    seeds[c] = int(seeds[c])



if pt_2:
    seeds2 = []
    for c,v in enumerate(seeds):
        if np.mod(c,2) == 0:
            for i in range(v, v+seeds[c+1]):
                seeds2.append(i)
        print(c, len(seeds)/2)
    seeds = seeds2

data.append("\n")
data = data[1:]

map_of_maps = []        
for c,v in enumerate(data):
    count = 1
    if "map" in v:
        while data[c+count] != "\n":
            count+=1
        else:
            map_of_maps.append(data[c+1:c+count])

print(seeds)
locations = []

for seed in seeds:
    for c,v in enumerate(map_of_maps):
        for cc,vv in enumerate(v):
            if (seed >= int(vv.split(" ")[1])) and (seed < int(vv.split(" ")[1])+int(vv.split(" ")[2])):
                seed = seed - int(vv.split(" ")[1]) + int(vv.split(" ")[0])
                break

    locations.append(seed)
            
        
print(np.min(locations))        
    
