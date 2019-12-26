# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:34:33 2019

@author: david

    Word gen should:
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
"""
import numpy as np
import random

wordlenmax = 6 # number of syllables
wordlenmin = 2 # number of syllables

syllenmax = 4 # number of letters
syllenmin = 3 # number of letters

wordlen = np.random.randint(low = wordlenmin, high = wordlenmax + 1) # random word length (doesn't include high val)

print("word length = %s" % (wordlen))
# print("syllable length = %s" %(syllen))

letlist = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")


word = "" # create emtpy syllable

for p in range(wordlen):
    syllen = np.random.randint(low = syllenmin, high = syllenmax + 1) # random syllable length (doesn't include high val)
    letarray = np.zeros(syllen, dtype=str) # create empty array
    
    for i in range(syllen): # populates array with random letters
        letarray[i] = random.choice(letlist)
        word += letarray[i] # combine letters into final syllable
    
    if p != wordlen - 1: # don't put a hyphen on the last syllable
        word += "-"
        
print(word)

"Success! I now have a randomly generated word with a random number of syllables and varying syllable length!"