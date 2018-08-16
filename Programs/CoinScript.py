# I can import my Simulations file
import Simulations as Sim
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Now I'll simulate flipping a biased coin 1000 times
Flips = []

for i in range(1000):
    Flips.append(Sim.CoinFlip(.41))
    print i

# Now I'll plot the outcome
Outcomes = pd.DataFrame(Flips,columns = ['Flip'])

sns.set(style="darkgrid")
sns.countplot(x = "Flip", data = Outcomes)
plt.show()
