"""
LackHaus
Advent of code day 11!
"""


import numpy as np
f = open("day11.txt")

data = f.readlines()
for c,v in enumerate(data):
    data[c] = data[c].strip("\n")
        
mat = np.zeros((len(data), len(data[0]))).astype(str)

for c,v in enumerate(data):
    for cc,vv in enumerate(v):
        mat[c,cc] = vv


empty_lines = []

empty_columns = []

for i in range(mat.shape[1]): #parse lines
    if not "#" in mat[i,:]:
        empty_lines.append(i)
for i in range(mat.shape[0]): #parse cols
    if not "#" in mat[:,i]:
        empty_columns.append(i)

print(mat.shape)
print(empty_lines, empty_columns)
k=0
for i in empty_lines:
    i = k+i
    new_line = []
    for j in range(mat.shape[1]):
        new_line.append(".")
    mat = np.insert(mat, i, new_line, axis = 0)
    k+=1

k=0
for i in empty_columns:
    i = k+i
    new_line = []
    for j in range(mat.shape[0]):
        new_line.append(".")
    mat = np.insert(mat, i, new_line, axis = 1)
    k+=1


hash_locations = []

for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        if mat[i,j] == "#":
            hash_locations.append([i,j])
            
def dist_between_hashes(c1, c2):
    dist = np.abs(c2[1] - c1[1]) + np.abs(c2[0] - c1[0])
    return dist

sum = 0
for c,v in enumerate(hash_locations):
    for c2,v2 in enumerate(hash_locations):
        if c2 != c:
            sum += dist_between_hashes(v,v2)
            print()
print(int(sum/2))



