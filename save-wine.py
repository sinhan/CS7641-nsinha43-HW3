#"!/usr/bin/python3

import csv
import sys
import subprocess
import numpy as np
import pandas as pd

###############################################

data = pd.read_csv('winequality-data.csv')

bins = [1,5,10]
quality_labels=[0,1]
data['quality_categorical'] = pd.cut(data['quality'], bins=bins, labels=quality_labels, include_lowest=True)
data=data.drop(['id'], axis =1)
data=data.drop(['quality'], axis =1)

export_csv = data.to_csv(r'wine.csv', index = None , header = False) #Don't forget to add '.csv' at the end of the path

