"""
LackHaus
Advent of code day 8!
"""

pt_2 = True

if not pt_2:
    f = open("day8.txt", "r")
    data = f.readlines()
    instructions = data[0].strip("\n")
    data = data[2:]
    loc = "AAA"
    steps = 0
    while loc != "ZZZ":
        for i in instructions:
            for c,v in enumerate(data):
                if loc in v.split("=")[0]:
                    if i == "R":
                        loc = v.split("(")[1].split(")")[0].split(", ")[1]
                        steps +=1
                        break
                    if i == "L":
                        loc = v.split("(")[1].split(")")[0].split(", ")[0]
                        steps += 1
                        break

    print(steps)

else:

    def all_end_in_z(l):
        count = 0
        for c, v in enumerate(l):
            if v[-1] == "z":
                count += 1
        if count == len(l):
            return True
        else:
            return False


    f = open("day8.txt", "r")
    data = f.readlines()
    instructions = data[0].strip("\n")
    data = data[2:]
    nodes = []
    for c,v in enumerate(data):
        if v.split(" = ")[0][-1] == "A":
            nodes.append(v.split(" = ")[0])
    steps = 0

    node_cycles = []
    for i in range(len(nodes)):
        node_cycles.append([])
    print(node_cycles)
    while not all_end_in_z(nodes):
        for i in instructions:
            for c,v in enumerate(nodes):
                for c2,v2 in enumerate(data):
                    if v in v2.split("=")[0]:
                        if i == "R":
                            nodes[c] = v2.split("(")[1].split(")")[0].split(", ")[1]
                            if c2 not in node_cycles[c]:
                                node_cycles[c].append(c2)
                                print(node_cycles)
                            steps += 1
                            break
                        if i == "L":
                            nodes[c] = v2.split("(")[1].split(")")[0].split(", ")[0]
                            if c2 not in node_cycles[c]:
                                node_cycles[c].append(c2)
                                print(node_cycles)
                            steps += 1
                            break





