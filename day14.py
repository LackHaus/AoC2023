import numpy as np


data = open("day14.txt").readlines()
print(data)

data2 = []
for i in data:
    data2.append(i.strip("\n"))
    
a = np.zeros((len(data2), len(data2[0]))).astype(str)

for i in range(a.shape[1]):
    for j in range(a.shape[0]):
        a[i,j] = data2[i][j]
        
stop = []   
for i in range(a.shape[1]):
    stop.append("#")

stop = np.array(stop)

b = np.insert(a,0,stop,axis=0)
print(b[1:,:])

for i in range(1,b.shape[0]):
    for j in range(b.shape[1]):
        if (b[i,j] == "O"):
            ii = 1
            while True:
                if b[i-ii,j] == ".":
                    ii+=1
                else:
                    if ii == 1:
                        break
                    else:
                        b[i-ii+1,j] = "O"
                        b[i,j] = "."
                        break
            print(b[1:,:])
                    
c = b[1:,:]
ans = 0
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        if c[i,j] == "O":
            ans += c.shape[1]-i
            
print(ans)