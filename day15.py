import numpy as np
f = open("day15.txt")
d = f.readlines()
x = []
for i in d:
    d2 = i.strip("\n")
    y = d2.split(",")
    for j in y:
        if j != "":
            x.append(j)

ans = 0
print(x)
for i in x:
    cv = 0
    for j in i:
        cv += ord(j)       
        cv = cv*17
        cv = np.mod(cv,256)
    ans+=cv
    
        
        
print(ans)
    