"""
LackHaus
Advent of code day 4!
"""

import numpy as np

pt_2 = False

f = open("day4.txt")
data = f.readlines()

match_scores = []
for c,v in enumerate(data):
    wins = []
    mine = []

    a = v.split(":")[1]
    b = a.split("|")[0]
    c = a.split("|")[1]
    wins = b.split(" ")
    mine = c.split(" ")
    wins_rem = 0
    mine_rem = 0
    for cc,vv in enumerate(wins):
        if vv == "" or vv == "\n":
            wins_rem += 1
    
    for cc,vv in enumerate(mine):
        if vv == "" or vv == "\n":
            mine_rem += 1
            
    for i in range(wins_rem):
        wins.remove("")
            
    for i in range(mine_rem):
        mine.remove("")
    

    for cc,vv in enumerate(wins):
        wins[cc] = int(wins[cc])
    for cc,vv in enumerate(mine):
        mine[cc] = int(mine[cc])
        
    
    match_count = 0
    for cc,vv in enumerate(wins):
        for ccc,vvv in enumerate(mine):
            if vv == vvv:
                match_count += 1
    
    if pt_2 == False:
        if match_count > 0:
            match_scores.append(2**(match_count-1))
        else:
            match_scores.append(0)
    if pt_2 == True:
        match_scores.append(match_count)

if pt_2 == False:
    print(np.sum(match_scores))

if pt_2 == True:

    match_scores = np.array(match_scores)
    
    
    
    card_inst = np.ones(len(match_scores))
    
    for c,v in enumerate(match_scores):
        if v != 0:
            card_inst[c+1:c+v+1] += card_inst[c]
    
    
    
                
    
    print(np.sum(card_inst))
            