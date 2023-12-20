"""
LackHaus
Advent of code day 2!
"""

import numpy as np
pt_2 = True

if not pt_2:
    f = open("day2.txt", "r")

    data = f.readlines()
    no_games = len(data)

    max_r = 12
    max_g = 13
    max_b = 14
    games = []
    new_data = []
    for i in data:
        new_data.append(i.split("\n"))

    for c,v in enumerate(new_data):
        x = v[0].split(":")
        y = [x[0],x[1].split(";")]
        for c2,v2 in enumerate(y[1]):
            red_loc = v2.find("red")
            green_loc = v2.find("green")
            blue_loc = v2.find("blue")


            if (red_loc != -1) and (int(v2[red_loc-3:red_loc-1])>max_r):
                games.append(int(y[0].split(' ')[-1]))
                break
            if (green_loc != -1) and (int(v2[green_loc-3:green_loc-1])>max_g):
                games.append(int(y[0].split(' ')[-1]))
                break
            if (blue_loc != -1) and (int(v2[blue_loc-3:blue_loc-1])>max_b):
                games.append(int(y[0].split(' ')[-1]))
                break


    print(np.sum(np.arange(1,no_games+1)) - np.sum(games))

else:
    f = open("day2.txt", "r")

    data = f.readlines()
    powers = 0
    new_data = []
    for i in data:
        new_data.append(i.split("\n"))

    for c, v in enumerate(new_data):
        x = v[0].split(":")[1].split(";")
        reds = []
        greens = []
        blues = []
        for c2, v2 in enumerate(x):

            if int(v2.find("red")) != -1:
                reds.append(int(v2[v2.find("red") - 3:v2.find("red") - 1]))
            else:
                reds.append(0)
            if int(v2.find("green")) != -1:
                greens.append(int(v2[v2.find("green") - 3:v2.find("green") - 1]))
            else:
                greens.append(0)
            if int(v2.find("blue")) != -1:
                blues.append(int(v2[v2.find("blue") - 3:v2.find("blue") - 1]))
            else:
                blues.append(0)
        max_red = np.max(reds)
        max_green = np.max(greens)
        max_blue = np.max(blues)

        powers += max_red * max_green * max_blue

    print(powers)