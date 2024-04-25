import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import DataFrameHandler as DFH

fileName = "WineQT.csv"

dfh = DFH.DataFrameHandler(fileName)

dfh.printSingleHistogram("quality",0)
dfh.printSingleHistogram("quality",1)
dfh.printSingleHistogram("quality",2)
#dfh.printBoxPlots("quality",0)
#dfh.printBoxPlots("quality",1)

dfh.printScatterPlot("residual sugar","alcohol",0)
dfh.printScatterPlot("fixed acidity","citric acid",0)
dfh.printScatterPlot("chlorides","density",0)
dfh.printScatterPlot("alcohol","density",0)
dfh.printScatterPlot("residual sugar","density",0)
dfh.printScatterPlot("pH","fixed acidity",0)


dfh.printObjectsPerClass("quality")

#fig, ax = plt.subplots()
#ax.boxplot(dfh.dataFrame["quality"])

plt.show()

#dataFrame.hist(figsize=(14,8))

#plt.boxplot(dataFrame["alcohol"])
#plt.scatter(dataFrame["citric acid"], dataFrame["fixed acidity"], color="blue", alpha=0.5)
#plt.figure(figsize=(8, 8))
#plt.pie(objectsBelongingToEachClass, labels=None, autopct='%1.1f%%', startangle=140)
#plt.title('Pie Chart')
#plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.legend(labels, loc="lower right")