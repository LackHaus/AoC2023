"""
LackHaus
Advent of code day 1!
"""

f = open("day1.txt", "r")
data = f.readlines()
pt2 = True
sum = 0
for i in data:
    d = []
    for count,value in enumerate(i):
        if value.isnumeric():
            d.append(value)
        if pt2:
            if i[count:].startswith("one"):
                d.append("1")
            elif i[count:].startswith("two"):
                d.append("2")
            elif i[count:].startswith("three"):
                d.append("3")
            elif i[count:].startswith("four"):
                d.append("4")
            elif i[count:].startswith("five"):
                d.append("5")
            elif i[count:].startswith("six"):
                d.append("6")
            elif i[count:].startswith("seven"):
                d.append("7")
            elif i[count:].startswith("eight"):
                d.append("8")
            elif i[count:].startswith("nine"):
                d.append("9")
    sum += int(d[0] + d[-1])
print(sum)