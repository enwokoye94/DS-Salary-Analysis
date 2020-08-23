import pickle
import pandas as pd


file_name = '../test_dat.p'
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    test_data=data['test_data']


test = list(test_data.iloc[1,:])  # taking one record as a test value
# print(test)