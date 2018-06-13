#!/usr/bin/env python3

import pandas as pd
import matplotlib.pylab as plt
plt.switch_backend('agg')

data = pd.read_csv("data/nlinfo.csv", names=['places','gdd'])

plt.bar(data['places'], data['gdd'], color='grey')
plt.xticks(rotation=45)
plt.title("Minimun GDD for Seed Growth in NL")
plt.ylabel("10 Year Average Annual GDD (1995-2004)")
plt.axhline(y=1342, color="yellow", label="Canary")
plt.axhline(y=1603, color="red", label="Flax")
plt.axhline(y=1432, color="green", label="Canola (B. napus)")
plt.axhline(y=1249, color="blue", label="Canola (B. rapa)")
plt.axhline(y=1509, color="orange", label="CMustard (B. juncea)")
plt.axhline(y=1521, color="purple", label="CMustard (S. alba)")
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('data/nlseedplot.png',index=False)
