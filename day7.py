"""
LackHaus
Advent of code day 7!
"""

import numpy as np

pt_2 = False

global card_order
if pt_2 == False:
    card_order = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))
else:
    card_order = list(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))

f = open("day7.txt", "r")
data = f.readlines()

hands = []
bids = []
values = []

for v in data:
    hands.append(v.split(" ")[0])
    bids.append(int(v.split(" ")[1]))

def read_hand(hand):

    x = 0
    hand_dict = {}
    for i in hand:
        if i not in hand_dict:
            hand_dict[i] = 1
        else:
            hand_dict[i] = hand_dict[i] + 1


    five, four, three, two, one = 0,0,0,0,0
    for card in hand_dict:
        if hand_dict[card] == 1:
            one+=1
        elif hand_dict[card] == 2:
            two+=1
        elif hand_dict[card] == 3:
            three+=1
        elif hand_dict[card] == 4:
            four+=1
        elif hand_dict[card] == 5:
            five+=1

        if one == 5:
            x=0
        elif two == 1:
            if one == 3:
                x=1
            else:
                x=4
        elif two == 2:
            x=2
        elif three == 1:
            if one == 2:
                x=3
        elif four == 1:
            x=5
        else:
            x=6



    value = 0
    for c,v in enumerate(hand):
        value += card_order.index(v)*len(card_order)**(4-c)
    value += x*len(card_order)**5

    return value

for i in hands:
    values.append(read_hand(i))


rank = 1
ranks = np.zeros(len(hands))
sorted_values = np.sort(values)

for c,v in enumerate(sorted_values):
    ranks[values.index(v)] = c+1

ans = 0
for c,v in enumerate(bids):
    ans += v*ranks[c]
print(int(ans))