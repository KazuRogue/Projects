# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:34:33 2019

@author: david

    Wordgen should:
    Generate an original, unique word
    Use combination of syllables made of combination of letters
    Generate a variety of word lengths and syllable lengths
    Adhere to phonotactic constraints

Notes

example: Zeltellsrazorious
Zel-tell-sra-zor-ious

number of possible letters = 26
number of possible syllables ~ 15,831
    ... Let's use letters

"The English language has 6 syllable types: Open, Closed, R-controlled, Vowel Team, Silent-e, and C-le."

    Now wordgen should:
    use syllables with an onset, nucleus, and coda.    

"""
import numpy as np
import random
import tkinter as tk
from tkinter import *

# ground work and definitions:


# random number between 1 and 100
def dice():
    return np.random.randint(1,100)

wordlenmax = 4 # number of syllables
wordlenmin = 1 # number of syllables

vowels = ("a", "e", "i", "o", "u", "y")

consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")


# for rules in allowed letter combinations in onset
onsetCC = ("bl", "br", "cl", "cr", "dr", "dw", "fl", "fr", "gl", "gr", "kl", "kr", "pl", "pr", "sc", "sh", "sk", "sl", "sm", "sn", "sp", "sq", "st", "sw", "th", "tr", "tw", "vl", "wr", "wh")
onsetCCC = ("scr", "shr", "sch", "spl", "spr", "str", "thr")

# for rules in allowed letter combinations in coda
codaCC = ("bl", "br", "bs", "ch", "ck", "cs", "ct", "cr", "cl", "dg", "ds", "dl", "dr", "fs", "ft", "fl", "gh", "gs", "gl", "kl", "kr", "ks", "kt", "lb", "lc", "ld", "lf", "jr", "jl", "jr", "mb", "mn", "ms", "mt", "mp", "nd", "ng", "nk", "nl", "nt", "ph", "pl", "pr", "pt", "rb", "rc", "rd", "rf", "rg", "rj", "rk", "rl", "rm", "rn", "rp", "rs", "rt", "sh", "sk", "sp", "st", "vl", "vr", "wb", "wc", "wd", "wf")


# creating the word:

word = "" # create emtpy word
localword = ""

def mkword():
    # localiterationcount = iterationcount
    wordlen = np.random.randint(low = wordlenmin, high = wordlenmax + 1) # random word length in syllables (doesn't include high val)

    localword = word    

    for p in range(wordlen): #loop will run once per syllable
       
        # the most common onset length should be 1, then 2 and 3
        result = dice()
        if result < 35:
                onsetlen = 0
        if 35 <= result < 70:
                onsetlen = 1
        if 70 <= result < 85:
                onsetlen = 2
        if 85 <= result:
                onsetlen = 3
                
        print("result = " + str(result))
                
        print("onsetlen = " + str(onsetlen))
                
        # the nucleus length will be 0, 1, or 2 (random)
        nucleuslen = np.random.randint(low = 1, high = 3)
        print("nucleuslen = " + str(nucleuslen))
        
        # the coda length will be 0, 1, 2, or 3 (random)
        codalen = np.random.randint(low = 0, high = 3)
        print("codalen = " + str(codalen))
        print()
    # onset
        if onsetlen == 1:
                localword += random.choice(consonants)
                
        if onsetlen == 2:
            onset = random.choice(onsetCC)
            localword += onset
        
        if onsetlen == 3:
            localword += random.choice(onsetCCC)
    
    # nucleus
        if nucleuslen == 1:
            localword += random.choice(vowels)
            
        if nucleuslen == 2:
            localword += random.choice(vowels) + random.choice(vowels)
            if localword[len(localword) - 2] == localword[len(localword) - 1]:
                print("------------ " + localword[:-1])
                localword = localword[:-1]
        
    # coda    
        if codalen == 1:
            localword += random.choice(consonants)
        
        if codalen == 2:
                localword += random.choice(codaCC)
                
    # syllable end
        if p != wordlen - 1: # don't put a hyphen on the last syllable
            localword += "-"
            
    print(localword)
    
mkword()

# window=Tk()
# window.title('gui')
# frame = Frame(master=window, width=300, height=100)

# var = StringVar()
# output = Text(window)
# output.insert(INSERT, "Hello")
# output.grid(pady = 10, row = 1, column = 0)

# iterationcount = 0


# wordbutton = Button(window, text = 'Make a word', command = lambda:[mkword()])
# wordbutton.grid(pady = 10, row = 0, column = 0)

# donebutton = Button(window, text = 'done', command = window.destroy)
# donebutton.grid(pady = 10, row = 3, column = 0)

# destroy = Button(window, text = "destroy", command = output.destroy())
# destroy.grid(pady = 10, row = 2, column = 0)





# frame.grid()

# window.mainloop()
