
import numpy as np
import pandas as pd

# data = ['huang', 'zhen', '1', '2']
# mySeries1 = pandas.Series(data=data)
# print(mySeries1)
# print(mySeries1[1])

# arr = ["Google", "Runoob", "Wiki"]
# mySeries2 = pandas.Series(arr, index = ["x", "y", "z"])
# print(mySeries2)
# print(mySeries2['y'])

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
mySeries3 = pd.Series(sites)
mySeries4 = pd.Series(sites, index = [1, 2])
mySeries5 = pd.Series(sites, index = [1, 2], name="RUNOOB-Series-TEST" )
print(mySeries3)
print(mySeries4)
print(mySeries5)







































