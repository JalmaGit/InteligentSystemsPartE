import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import DataFrameHandler as DFH

fileName = "WineQT.csv"

dataFrame = pd.read_csv(fileName)

dataFrame = dataFrame.drop_duplicates()

dataFrame = dataFrame.dropna(axis=0, how='all')

objectsBelongingToEachClass = np.empty(0)

for i in range(11):
    objectsBelongingToEachClass = np.append(objectsBelongingToEachClass,(dataFrame["quality"] == i).sum())
    print("When quality is",i,", the number of wines with said quality is:",(dataFrame["quality"] == i).sum())

labels = np.array(["Disgusting","Extremly Bad", "Very Bad", "Bad", "Kinda Bad", "Mediocre", "Decent", "Good", "Very Good", "Extremely Good", "Perfect"])

print(dataFrame.describe())

print(np.std(dataFrame["quality"]))

dataFrame.hist(figsize=(14,8))

#plt.boxplot(dataFrame["alcohol"])
#plt.scatter(dataFrame["citric acid"], dataFrame["fixed acidity"], color="blue", alpha=0.5)
#plt.figure(figsize=(8, 8))
#plt.pie(objectsBelongingToEachClass, labels=None, autopct='%1.1f%%', startangle=140)
#plt.title('Pie Chart')
#plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.legend(labels, loc="lower right")
plt.show()