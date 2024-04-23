import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import DataFrameHandler as DFH

fileName = "WineQT.csv"

dataFrame = pd.read_csv(fileName)

dataFrame = dataFrame.drop_duplicates()

dataFrame = dataFrame.dropna(axis=0, how='all')

for i in range(11):
    print("When quality is",i,", the number of wines with said quality is:",(dataFrame["quality"] == i).sum())

print(dataFrame.describe())

print(np.std(dataFrame["quality"]))

#plt.boxplot(dataFrame["alcohol"])
plt.scatter(dataFrame["citric acid"], dataFrame["fixed acidity"], color="blue", alpha=0.5)
plt.show()