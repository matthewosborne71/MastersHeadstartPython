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

def RandomWalk(p,NumSteps,Absorbing):

    # Start at 0
    CurrentPosition = 0

    # Initialize position list
    Positions = [CurrentPosition]

    # Take first Step
    Flip = CoinFlip(p)

    if Flip == "H":
        # If heads we step forward
        CurrentPosition = CurrentPosition + 1

    elif Flip == "T":
        # If tails we step back
        CurrentPosition = CurrentPosition - 1

    # Add our Current Position to the running list of positions
    Positions.append(CurrentPosition)

    if Absorbing == "Yes":

        for i in range(2,NumSteps):
            Flip = CoinFlip(p)

            if Flip == "H":
                # If heads we step forward
                CurrentPosition = CurrentPosition + 1

            elif Flip == "T":
                # If tails we step back
                CurrentPosition = CurrentPosition - 1

            # Add our Current Position to the running list of positions
            Positions.append(CurrentPosition)

            # Check if we hit 0
            if CurrentPosition == 0:
                Absorbed = "Yes"
                return Positions,Absorbed

        Absorbed = "No"
        return Positions,Absorbed


    elif Absorbing == "No":

        # For each step we'll flip a coin and check the outcome
        for i in range(2,NumSteps):
            Flip = CoinFlip(p)

            if Flip == "H":
                # If heads we step forward
                CurrentPosition = CurrentPosition + 1

            elif Flip == "T":
                # If tails we step back
                CurrentPosition = CurrentPosition - 1

            # Add our Current Position to the running list of positions
            Positions.append(CurrentPosition)

        return Positions
    else:
        print "Sorry Absorbing must be 'Yes' or 'No'"
