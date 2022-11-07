import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1):
gm = pd.read_csv("gm.bz2", sep="\t")

# loaded gm data

# 2):
print(gm.shape)
print(gm.head())


#There are 13055 rows and 25 columns.
#The first few line look pretty reasonable