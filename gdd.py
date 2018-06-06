#!/usr/bin/env python

import argparse
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument('data', action="store", type=str)
parser.add_argument('tbase', action="store", type=int)
parser.add_argument('tupper', action="store")

args = parser.parse_args()

data = pd.read_csv(args.data)
data = data.fillna(0)

for index, row in data.iterrows():
    print(row.loc['Max Temp (°C)'])
