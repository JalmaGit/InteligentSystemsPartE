import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import DataFrameHandler as DFH

def useDataFrameHandlerPlotting(dfh):
    #dfh.printSingleHistogram("quality",0)
    #dfh.printSingleHistogram("quality",1)
    #dfh.printSingleHistogram("quality",2)
    #dfh.printBoxPlots("quality",0)
    dfh.printBoxPlots("quality",1)

    #dfh.printScatterPlot("density",0)


    #dfh.printObjectsPerClass("quality")

    #fig, ax = plt.subplots()
    #ax.boxplot(dfh.dataFrame["quality"])

def histograms(df):

    goodDF = df[df['quality'] != 5]

    goodDF = goodDF.drop(columns='quality')      
    goodDF.hist()
    plt.suptitle("Good Wine")

    badDF = df[df['quality'] != 6]

    badDF = badDF.drop(columns='quality')       
    badDF.hist()
    plt.suptitle("Bad Wine")
    plt.show()

def removeOutliers(dfh):
    listOfFeatures = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]

    for feature in listOfFeatures:
        dfh.dataFrame = dfh.removeOutliers(dfh.dataFrame, feature)
        
def scatterPlot(dfh):

    pairplot = sns.pairplot(dfh.dataFrame, hue="quality")
    pairplot.map_offdiag(plt.scatter, cmap="coolwarm")
    plt.title('Pair Plot')
    plt.show()
    
fileName = "WineQT.csv"

dfh = DFH.DataFrameHandler(fileName)

#useDataFrameHandlerPlotting(dfh)

#plt.show()

# Scatter plot

#dfh.dataFrame.boxplot()
#plt.show()

#scatterPlot()

#for i, element in enumerate(dfh.dataFrame.columns):

    #dfh.printScatterPlot(element,1)

    #for col2 in dfh.dataFrame.columns[i+1:]:
        #plt.figure()
        #sns.scatterplot(data=dfh.dataFrame, x=col1, y=col2)
        #plt.title(f'Scatter Plot: {col1} vs {col2}')

# Heatmap
#dfh.dataFrame = dfh.dataFrame.drop(columns="quality")
#corr = dfh.dataFrame.corr()
#sns.heatmap(corr, annot=True, cmap='coolwarm')
#plt.title('Heatmap')
#plt.show()

# Boxplot
#sns.boxplot(data=dfh.dataFrame)
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