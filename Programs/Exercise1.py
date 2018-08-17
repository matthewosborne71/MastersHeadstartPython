# Write a program that generates a random integer between 1 and 100
# and then has the user guess the number until they get it correct.
import random

Number = random.randint(1,100)
Guess = -99

print "I thought of a number, want to guess? "

while Guess != Number:
    Guess = int(raw_input())

    if Guess != Number:
        print "You're wrong, loser. Guess again."

print "Way to go! You did it! Awesome!"
