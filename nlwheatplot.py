#!/usr/bin/env python3

import pandas as pd
import matplotlib.pylab as plt
plt.switch_backend('agg')

data = pd.read_csv("data/nlinfo.csv", names=['places','gdd'])

plt.bar(data['places'], data['gdd'], color='grey')
plt.xticks(rotation=45)
plt.title("Minimun GDD for Wheat Growth in NL")
plt.ylabel("10 Year Average Annual GDD 1995-2004)")
plt.axhline(y=1269, color="blue", label="Barley")
plt.axhline(y=1538, color="red", label="Wheat (Hard Red)")
plt.axhline(y=1483, color="green", label="Oat")
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('data/nlwheatplot.png',index=False)
