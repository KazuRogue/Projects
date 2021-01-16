import random
import numpy
#import matplotlib.pyplot

# Dice
# Roll two d20s and save the highest in an array

num_rolls = 1000000
adv = numpy.zeros(num_rolls)
disadv = numpy.zeros(num_rolls)
d20a_array = numpy.zeros(num_rolls)
d20b_array = numpy.zeros(num_rolls)

for i in range(num_rolls):
    d20a = random.randint(1,20)
    d20b = random.randint(1,20)
    if d20a >= d20b:
        adv[i] = d20a
        disadv[i] = d20b
    else:
        adv[i] = d20b
        disadv[i] = d20a
    d20a_array[i] = d20a
    d20b_array[i] = d20b
    #print(i)


print()
print("number of rolls =", num_rolls)
print()
print("Advantage:")
print("average roll =",sum(adv) / len(adv))
#print(adv)
print()
print("Disadvantage:")
print("average roll =",sum(disadv) / len(disadv))
print()
print("Straight d20 roll average =", ((sum(d20a_array) + sum(d20b_array)) / 2) / num_rolls)
#print(disadv)
#print("d20a =", d20a_array)
#print("d20b =", d20b_array)
print()