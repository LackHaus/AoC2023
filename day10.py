"""
LackHaus
Advent of code day 10!
"""

import numpy as np

f = open("day10.txt", "r")

data2 = f.readlines()

data = []

for i in data2:
    data.append(i.strip("\n"))

mat = np.zeros((len(data), len(data[0]))).astype(str)
for c,v in enumerate(data):
    for cc,vv in enumerate(v):
        mat[c,cc] = vv


loop = []
for j in range(mat.shape[1]): #parsing left to right, top to bottom [i,j] are coordinates
    for i in range(mat.shape[0]):
        if mat[i,j] == "S":
            loop.append([i,j])

while True:
    loop_length_b = len(loop)
    if mat[loop[-1][0], loop[-1][1]] == "S":
        if (mat[loop[-1][0], loop[-1][1]-1] in ["-", "L", "F"]) and ([loop[-1][0], loop[-1][1]-1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]-1])
        elif (mat[loop[-1][0], loop[-1][1]+1] in ["-", "7", "J"]) and ([loop[-1][0], loop[-1][1]+1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]+1])
        elif (mat[loop[-1][0]-1, loop[-1][1]] in ["|", "7", "F"]) and ([loop[-1][0]-1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0]-1, loop[-1][1]])
        elif (mat[loop[-1][0]+1, loop[-1][1]] in ["|", "L", "J"]) and ([loop[-1][0]+1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0]+1, loop[-1][1]])

    elif mat[loop[-1][0], loop[-1][1]] == "-":
        if (mat[loop[-1][0], loop[-1][1]-1] in ["-", "L", "F"]) and ([loop[-1][0], loop[-1][1]-1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]-1])
        elif (mat[loop[-1][0], loop[-1][1]+1] in ["-", "7", "J"]) and ([loop[-1][0], loop[-1][1]+1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]+1])
    elif mat[loop[-1][0], loop[-1][1]] == "|":
        if (mat[loop[-1][0]-1, loop[-1][1]] in ["|", "7", "F"]) and ([loop[-1][0]-1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0]-1, loop[-1][1]])
        elif (mat[loop[-1][0]+1, loop[-1][1]] in ["|", "L", "J"]) and ([loop[-1][0]+1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0]+1, loop[-1][1]])
    elif mat[loop[-1][0], loop[-1][1]] == "F":
        if (mat[loop[-1][0]+1, loop[-1][1]] in ["|", "L", "J"]) and ([loop[-1][0] + 1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0]+1, loop[-1][1]])
        elif (mat[loop[-1][0], loop[-1][1]+1] in ["-", "7", "J"]) and ([loop[-1][0], loop[-1][1]+1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]+1])
    elif mat[loop[-1][0], loop[-1][1]] == "J":
        if (mat[loop[-1][0], loop[-1][1]-1] in ["-", "L", "F"]) and ([loop[-1][0], loop[-1][1]-1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]-1])
        elif (mat[loop[-1][0]-1, loop[-1][1]] in ["|", "7", "F"]) and ([loop[-1][0]-1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0]-1, loop[-1][1]])
    elif mat[loop[-1][0], loop[-1][1]] == "L":
        if (mat[loop[-1][0], loop[-1][1]+1] in ["-", "7", "J"]) and ([loop[-1][0], loop[-1][1]+1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]+1])
        elif (mat[loop[-1][0]-1, loop[-1][1]] in ["|", "7", "F"]) and ([loop[-1][0]-1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0]-1, loop[-1][1]])
    elif mat[loop[-1][0], loop[-1][1]] == "7":
        if (mat[loop[-1][0], loop[-1][1]-1] in ["-", "L", "F"]) and ([loop[-1][0], loop[-1][1]-1] not in loop):
            loop.append([loop[-1][0], loop[-1][1]-1])
        elif (mat[loop[-1][0] + 1, loop[-1][1]] in ["|", "L", "J"]) and ([loop[-1][0] + 1, loop[-1][1]] not in loop):
            loop.append([loop[-1][0] + 1, loop[-1][1]])

    loop_length_a = len(loop)
    if loop_length_a == loop_length_b:
        break



if np.mod(len(loop),2) == 0:
    print(int(len(loop)/2))
else:
    print(int(1+len(loop)/2))





