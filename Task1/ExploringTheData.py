import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import DataFrameHandler as DFH

fileName = "WineQT.csv"

dfh = DFH.DataFrameHandler(fileName)

dfh.printSingleHistogram("quality")

dfh.dataFrame.info()

dfh.printObjectsPerClass("quality")

fig, ax = plt.subplots()
ax.boxplot(dfh.dataFrame["quality"])

dfh.dataFrame.info()
print(dfh.dataFrame.describe())

plt.show()

#dataFrame.hist(figsize=(14,8))

#plt.boxplot(dataFrame["alcohol"])
#plt.scatter(dataFrame["citric acid"], dataFrame["fixed acidity"], color="blue", alpha=0.5)
#plt.figure(figsize=(8, 8))
#plt.pie(objectsBelongingToEachClass, labels=None, autopct='%1.1f%%', startangle=140)
#plt.title('Pie Chart')
#plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.legend(labels, loc="lower right")