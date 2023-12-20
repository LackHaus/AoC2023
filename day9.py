"""
LackHaus
Advent of code day 9!
"""

f = open("day9.txt")

def has_only_zeros(l):
    count = 0
    for i in l:
        if i == 0:
            count += 1
    if count == len(l):
        return True
    else:
        return False

def convert_to_ints(l):
    l2 = []
    for i in l:
        l2.append(int(i))
    return l2


top_layers = f.readlines()

print(top_layers)
ans = 0

for top_layer in top_layers:
    top_layer = top_layer.split(" ")
    top_layer = convert_to_ints(top_layer)
    L = [top_layer]
    while has_only_zeros(L[-1]) != True:
        l = []
        for i in range(len(L[-1])-1):
            l.append(L[-1][i+1]-L[-1][i])
        L.append(l)


    for i in range(len(L)):
        if i == 0:
            L[-1].append(0)
        else:
            L[(i+1)*-1].append(L[(i+1)*-1][-1]+L[(i)*-1][-1])

    ans+=L[0][-1]

print(ans)






