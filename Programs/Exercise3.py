# Add code to the Simulations file to include a random walk. Make it so that the
# random walk has an "absorbing state" at position 0, so that if the random walk
# hits 0 it stays there and the walk is over

# Using Simulations write a script to run the Random Walk 100 times for different
# values of p. The goal is to see how p affects the percentage of walks that
# get absorbed. I.E. plot p on the x-axis and plot percentage of walks absorbed
# on the y-axis.

import Simulations as Sim
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Probs = np.arange(0,1,.01)
NumWalks = 1000
NumSteps = 1000
PercAbs = []



for p in Probs:
    print str(p)
    absorbed = []
    for i in range(NumWalks):

        pos,a = Sim.RandomWalk(p,NumSteps,"Yes")
        del pos
        absorbed.append(a)


    NumAbsorbed = float(absorbed.count("Yes"))
    PercAbsorbed = NumAbsorbed/float(NumWalks)
    PercAbs.append(PercAbsorbed)

plt.plot(Probs,PercAbs)
plt.show()
