#!/usr/bin/python

import sys
import os

def choose(my_region, rival_region, all_cards, cards_in_hands):
    
    return 1, 2

if __name__ == '__main__':
    my_region = [[] for i in range(9)]
    rival_region = [[] for i in range(9)]

    all_cards = {'A': [1]*10, 'B': [1]*10, 'C': [1]*10, 'D': [1]*10, 'E': [1]*10, 'F': [1]*10}

    cards_in_hands = []

    
    while True:
        n = int(sys.stdin.readline())
        #sys.stderr.write("demo %d n: %d\n" % (os.getpid(), n))
        over = False
        for i in range(n):
            cmd = sys.stdin.readline()
            sys.stderr.write("demo %d cmd: " % os.getpid()+ cmd)
            items = cmd.split()
            if items[0] == 'cardget':
                cards_in_hands.append(items[1])
                color = items[1][0]
                num = int(items[1][1])
                all_cards[color][num-1] = 0

            elif items[0] == 'rival':
                pass
            else:
                over = True
        if over:
            break
        else:

            
            for i in range(9):
                if len(my_region[i]) < 3:
                    reg_idx = i
                    my_region[i].append(cards_in_hands[0])
                    break

            i, j = choose(my_region, rival_region, all_cards, cards_in_hands)                
            sys.stdout.write("act %d %s\n" % (reg_idx, cards_in_hands[0]))
            sys.stdout.flush()
            sys.stderr.flush()            
            cards_in_hands = cards_in_hands[1:]
            
