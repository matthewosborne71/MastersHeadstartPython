# Simulations includes a number of functions that can be used in game of chance
# simulations.
import random

def CoinFlip(p):
    flip = random.random()

    if flip < p:
        return "H"
    else:
        return "T"

def DiceRoll(sides):
    roll = random.random()

    for i in range(sides):
        if roll < float(i+1)/float(sides):
            return str(i+1)
