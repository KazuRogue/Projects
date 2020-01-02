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

# ground work and definitions:


# random number between 1 and 100
def dice():
    return np.random.randint(1,100)

wordlenmax = 4 # number of syllables
wordlenmin = 1 # number of syllables

wordlen = np.random.randint(low = wordlenmin, high = wordlenmax + 1) # random word length in syllables (doesn't include high val)

vowels = ("a", "e", "i", "o", "u", "y")

consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")


# for rules in allowed letter combinations in onset
onsetCC = ("s", "C")
onsetCCC1 = ("p", "t", "k")
onsetCCC2 = ("l", "r", "u", "w")

# for rules in allowed letter combinations in coda
codaCC1 = ("m", "n", "l", "r", "s")
codaCC2 = ("s", "z", "t", "d", "th")

word = "" # create emtpy word


# creating the word:


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
    codalen = np.random.randint(low = 0, high = 4)
    print("codalen = " + str(codalen))
    print()
# onset
    if onsetlen == 1:
            word += random.choice(consonants)
            
    if onsetlen == 2:
        onset = random.choice(onsetCC)
        if onset == "s":
            word += "s" + random.choice(consonants)
        if onset == "C":
            word += random.choice(consonants) + random.choice(onsetCCC2)
    
    if onsetlen == 3:
        word += "s" + random.choice(onsetCCC1) + random.choice(onsetCCC2)

# nucleus
    if nucleuslen == 1:
        word += random.choice(vowels)
        
    if nucleuslen == 2:
        word += random.choice(vowels) + random.choice(vowels)
    
# coda    
    if codalen == 1:
        word += random.choice(consonants)
    
    if codalen == 2:
        codachance = np.random.randint(low = 0, high = 1)
        if codachance == 0:
            word += random.choice(codaCC1) + random.choice(consonants)
        else: word += random.choice(consonants) + random.choice(codaCC2)
    
    if codalen == 3:
        word += random.choice(codaCC1) + random.choice(consonants) + random.choice(codaCC2)
    
# syllable end
    if p != wordlen - 1: # don't put a hyphen on the last syllable
        word += "-"
        
print(word)