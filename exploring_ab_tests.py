import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


df = pd.read_csv('cleaned_list.csv')
print(df.columns)

print(df.nuique())
