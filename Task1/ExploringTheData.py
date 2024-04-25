import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import DataFrameHandler as DFH

def useDataFrameHandlerPlotting(dfh):
    dfh.printSingleHistogram("quality",0)
    dfh.printSingleHistogram("quality",1)
    dfh.printSingleHistogram("quality",2)
    dfh.printBoxPlots("quality",0)
    dfh.printBoxPlots("quality",1)

    #dfh.printScatterPlot("density",0)


    dfh.printObjectsPerClass("quality")

    #fig, ax = plt.subplots()
    #ax.boxplot(dfh.dataFrame["quality"])
    
fileName = "WineQT.csv"

dfh = DFH.DataFrameHandler(fileName)

useDataFrameHandlerPlotting(dfh)

# Scatter plot
#pairplot = sns.pairplot(dfh.dataFrame, hue="quality")
#pairplot.map_offdiag(plt.scatter, cmap="coolwarm")
#plt.title('Pair Plot')

for i, element in enumerate(dfh.dataFrame.columns):

    dfh.printScatterPlot(element,1)

#    for col2 in dfh.dataFrame.columns[i+1:]:
 #       plt.figure()
  #      sns.scatterplot(data=dfh.dataFrame, x=col1, y=col2)
   #     plt.title(f'Scatter Plot: {col1} vs {col2}')

# Heatmap
corr = dfh.dataFrame.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()

# Boxplot
#sns.boxplot(data=dfh.dataFrame, x="species", y="petal_width")
#plt.title('Boxplot')
#plt.show()

#dataFrame.hist(figsize=(14,8))

#plt.boxplot(dataFrame["alcohol"])
#plt.scatter(dataFrame["citric acid"], dataFrame["fixed acidity"], color="blue", alpha=0.5)
#plt.figure(figsize=(8, 8))
#plt.pie(objectsBelongingToEachClass, labels=None, autopct='%1.1f%%', startangle=140)
#plt.title('Pie Chart')
#plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.legend(labels, loc="lower right")