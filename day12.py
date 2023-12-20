"""
LackHaus
Advent of code day 12!
"""

f = open("day12.txt", "r")
data = f.readlines()


def check_line(line):
    numbers = line.split(" ")[1]
    nums = numbers.split(",")
    x = line.split(" ")[0].split(".")
    count = 0
    y = x
    
    ci = 0
    for c,v in enumerate(y):
        if (v == "") or (v == "\n"):
           ci+=1
    
    for i in range(ci):
        y.remove("")
    
    if len(y) != len(nums):
        return False
    
    
    for i in x:
        if "#" in i:
            if len(i) == int(nums[count]):
                count += 1
            else:
                return False
    return True

        
import itertools
def get_combinations(lst): # creating a user-defined method
   combination = [] # empty list 
   for r in range(1, len(lst)+1):
      # to generate combination
      combination += itertools.combinations(lst, r)
   return combination

tot = 0
for line in data:
    line_tot = 0
    null_line = list(line)
    for c,v in enumerate(null_line):
        if v == "?":
            null_line[c] = "."
    null_line = "".join(null_line)

    if check_line(null_line):
        line_tot += 1
    com = 0

    inter = []
    for c,v in enumerate(line):
        if v == "?":
            inter.append(c)

    com = get_combinations(inter)
    for i in com:

        new_line = line
        new_line = list(new_line)
        for j in i:
            new_line[j] = "#"

        for c2,v2 in enumerate(new_line):
            if v2 == "?":
                new_line[c2] = "."
        new_line = "".join(new_line)
        if check_line(new_line):
            line_tot+=1

    print(line_tot)
    tot += line_tot
    
            
            
print(tot)
        
        

