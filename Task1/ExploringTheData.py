import pandas as pd
import DataFrameHandler as DFH

fileName = "WineQT.csv"

dataFrame = pd.read_csv(fileName)

print(dataFrame.describe())

for i in range(11):
    print("When quality is",i,", the number of wines with said quality is:",(dataFrame["quality"] == i).sum())

print(dataFrame)