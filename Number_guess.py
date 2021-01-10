# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:00:00 2021

@author: hamad
"""

import random
import math
import time

#Taking inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

#Generating random number between the lower and upper bound
x = random.randint(lower,upper)

#Giving instructions about the number of chances that depend on the range
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)),"chances to guess the integer!\n")

#Initializing the number of guesses
count = 0

#Calculating the mininum number of guesses
while count < math.log(upper - lower + 1, 2):
    count += 1
   
    #Taking guess as input
    guess = int(input("Guess a number: "))
    
    #Condition testing
    if x == guess:
        print("Congratulations you did it in", count, "chance/s")
        time.sleep(5) #Delaying break
        #Once guessed break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

    #If guessing more than the required chances show this output
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d"%x)
        time.sleep(2)
        print("\tBetter Luck Next time!")
        time.sleep(5)