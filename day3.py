"""
LackHaus
Advent of code day 3!
"""

import numpy as np
f = open("day3.txt",'r')
data = f.readlines()

data2 = []

for i in data:
    data2.append(i.strip("\n"))

print(data2)

problems = []
problem_nos = []
for c,v in enumerate(data2):
    for cc,vv in enumerate(v):
        if vv.isnumeric():
            for i in [-1,0,1]:
                if (c+i > -1) and (c+i < len(data2)):
                    for j in [-1,0,1]:
                        if (cc+j > -1) and (cc+j < len(data2)):
                            if (data2[c+i][cc+j].isnumeric() == False) and (data2[c+i][cc+j] != "."):
                                problems.append((c,cc))
                                ii = 0
                                while data2[c][cc-ii].isnumeric():
                                    ii += 1
                                jj = 0
                                while data2[c][cc+jj].isnumeric():
                                    jj += 1
                                problem_nos.append(int(data2[c][cc-ii+1:cc+jj]))




for count,num in enumerate(problem_nos):
    if problem_nos[count] == problem_nos[count+1]:
        problem_nos.remove(num)




print(problem_nos)
all_nos = []
data3 = []
#for c,v in enumerate(data2):
   # for num in data3.append(v.split(".")):
        #if num.isnumerical():
            #all_nos.append(int(num))

print(np.sum(problem_nos))




