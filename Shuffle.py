"""
This is a script to simulate shuffling a deck of cards.

Objectives:
1 simulate shuffling a deck of cards
2 determine how many shuffles are 'enough' to randomize the deck

""" 

import random


deck = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
#deck = ['h1','h2','h3','h4','h5','h6','h7','h8','h9','h10','hJ','hQ','hK','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','dJ','dQ','dK','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','sJ','sQ','sK','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','cJ','cQ','cK']

number_of_shuffles = 0

loop = True

def shuffle():
    
    print()
    global number_of_shuffles
    if number_of_shuffles == 0:
        print("Unshuffled deck:")
        print(deck)
        print()

    half = len(deck)//2 # Split deck in half (preparing to shuffle)
    left = deck[:half]
    right = deck[half:]

    # The number of cards that fall consecutively from one side of the shuffle is a group (a perfect shuffle would have all groups of one)
    group_thickness = random.randint(1,3)


    # Groups fall into the deck starting with the left hand of the shuffle and then alternating right and left
    count = 0
    side_switch_count = 0
    left_count = 0
    right_count = 0
    halt_left = False
    halt_right = False
    halt_side_switch = False
    for i in range(0, len(deck)): # For every card in the deck
        count += 1 # Place in group
        ''' Diagnostic
        print()
        print("start")
        print(i)
        print("count =", count)
        print("group thickness =", group_thickness)
        '''

        if side_switch_count % 2 == 0 and left_count < len(left) and halt_left is False: # The group falls from the left and right sides alternately
            side = "left"
            if i == 0:
                deck[- 1] = left[-1]
            if i != 0:
                deck[- i - 1] = left[- left_count - 1]
            #print("card chosen from left =", left[- left_count])
            left_count += 1 # Keeps track of how many cards have fallen from the left side
            if left_count == half:
                group_thickness = count
                halt_left = True

        if side_switch_count % 2 != 0 and right_count < len(right) and halt_right is False:
            side = "right"
            if i == 0:
                deck[- 1] = right[-1]
            if i != 0:
                deck[- i - 1] = right[- right_count - 1]
            #print("card chosen from right", right[- right_count])
            right_count += 1 # Keeps track of how many cards have fallen from the right side
            if right_count == half:
                group_thickness = count
                halt_right = True

        ''' Diagnostic
        print("left count =", left_count)
        print("right count =", right_count)
        print("halt_left =", halt_left)
        print("halt_right =", halt_right)
        print(side)

        print()
        '''

        if count == group_thickness and halt_side_switch == False: # If the card is the last card in the group, start the next group
            group_thickness = random.randint(1,3)
            count = 0
            side_switch_count += 1 # Increases when the next group is about to fall from the opposite side
        
        if halt_right == True or halt_left == True:
            halt_side_switch = True

        ''' Diagnostic
        print("halt_side_switch =", halt_side_switch)
        print(deck)
        print(left)
        print(right)
        print("finish")
        '''

    number_of_shuffles += 1
    print("Number of shuffles:", number_of_shuffles)
    print(deck)
    print()


function_dict = {'shuffle': shuffle, '': shuffle, 'q': exit} # Linking input commands with functions



while loop: # Input command to run function

    try:
        print()
        print("(Press Enter to shuffle, or type q to quit)")
        func = input('Input command: ')
        function_dict[func]()
        print()
    except KeyError:
        continue
    except KeyboardInterrupt: # This isn't working for some reason...
        print("All done")
        raise