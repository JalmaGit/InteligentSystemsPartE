import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataFrameHandler:

    def __init__(self, fileName):
        self.dataFrame = pd.read_csv(fileName)
        self.dataFrame = self.dataFrame.drop_duplicates()
        self.dataFrame = self.dataFrame.dropna(axis=0, how='all')
        self.dataFrame = self.dataFrame.dropna(axis=1, how='any')
        self.dataFrame = self.dataFrame.drop(columns=["Id"])

        self.notUsedDataFrame = pd.read_csv(fileName)
        self.notUsedDataFrame = self.notUsedDataFrame.drop_duplicates()
        self.notUsedDataFrame = self.notUsedDataFrame.dropna(axis=0, how='all')
        self.notUsedDataFrame = self.notUsedDataFrame.dropna(axis=1, how='any')
        self.notUsedDataFrame = self.notUsedDataFrame.drop(columns=["Id"])
 
        dataToReplace = []
        for quality in self.dataFrame["quality"]:
            if quality <= 5:
                dataToReplace.append(5)
            else:
                dataToReplace.append(6)
        
        self.dataFrame["quality"] = dataToReplace

        print(self.dataFrame)
        print(self.dataFrame.describe())

    def printObjectsPerClass(self, feature):
        objectsBelongingToEachClass = np.empty(0)

        #labels = np.array(["Disgusting","Extremly Bad", "Very Bad", "Bad", "Kinda Bad", "Mediocre", "Decent", "Good", "Very Good", "Extremely Good", "Perfect"])
        labels = np.array(["Bad","Good"])

        for i in range(5,7):
            objectsBelongingToEachClass = np.append(objectsBelongingToEachClass,(self.dataFrame[feature] == i).sum())
            print("When quality is",i,", the number of wines with said quality is:",(self.dataFrame[feature] == i).sum(),labels[i-5])

    def printSingleHistogram(self, feature, selector, binLimit: bool = False):
        columnData = self.dataFrame[feature]

        fig, ax = plt.subplots()

        if (feature == "quality") and (selector == 0):
            customBins = np.arange(4, 9, 1)
            ax.set_xlabel('Quality')
            ax.set_ylabel('Frequency')
            ax.set_title('Histogram Of Quality')
            ax.hist(columnData, customBins)
        elif ((feature == "quality") and (selector == 1)):
            columnData = self.notUsedDataFrame[feature]
            customBins = np.arange(11)
            ax.set_xlabel('Quality')
            ax.set_ylabel('Frequency')
            ax.set_title('Histogram Of Quality')
            ax.hist(columnData, customBins)
        elif (selector == 2):
            self.dataFrame.hist()
        else:
            ax.hist(columnData)

        fig.show()

    def printBoxPlots(self, feature, selector):


        if selector == 0:
            fig1, ax1 = plt.subplots()
            ax1.boxplot(self.dataFrame[feature])
            fig1.show()

        if selector == 1:
            listOfFeatures = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]
            for i in listOfFeatures:
                fig1, ax1 = plt.subplots()
                ax1.set_xlabel(i)
                ax1.set_ylabel('Frequency')
                label = "Box plot of " + i
                ax1.set_title(label)
                ax1.boxplot(self.dataFrame[i])
                fig1.show()

    def printScatterPlot(self, featureToCompare, selector):

        if selector == 0:
            listOfFeatures = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "pH", "density", "sulphates", "alcohol", "quality"]
            listOfFeatures.remove(featureToCompare)

            numPlots = len(listOfFeatures)
            numCols = 3
            numRows = 4
            
            figs, axs = plt.subplots(numRows, numCols, figsize=(30,10))

            if numPlots == 1:
                axs = [axs]

            for i, element in enumerate(listOfFeatures):
                row = i // numCols
                col = i % numCols
                scatterGood = []
                scatterBad = []
                compareGoodFeature = []
                compareBadFeature = []

                for quality, element1, compareElement in zip(self.dataFrame["quality"],self.dataFrame[element],self.dataFrame[featureToCompare]):
                    if quality <= 5:
                        scatterBad.append(element1)
                        compareBadFeature.append(compareElement)
                    else:
                        scatterGood.append(element1)
                        compareGoodFeature.append(compareElement)
                
                axs[row][col].scatter(scatterBad, compareBadFeature, label="Bad Wine")
                axs[row][col].scatter(scatterGood, compareGoodFeature, alpha=0.5, label="Good Wine")
                axs[row][col].set_xlabel(element)
                axs[row][col].set_ylabel(featureToCompare)
                label = "Scatter plot of " + element + " vs "  + featureToCompare
                axs[row][col].set_title(label)
                axs.legend()
            
            plt.subplots_adjust(wspace=0.4, hspace=0.4)
                
            figs.show()

        if selector == 1:
            listOfFeatures = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "pH", "density", "sulphates", "alcohol", "quality"]
            listOfFeatures.remove(featureToCompare)
            
            for element in listOfFeatures:
                figs, axs = plt.subplots()
                scatterGood = []
                scatterBad = []
                compareGoodFeature = []
                compareBadFeature = []

                for quality, element1, compareElement in zip(self.dataFrame["quality"],self.dataFrame[element],self.dataFrame[featureToCompare]):
                    if quality <= 5:
                        scatterBad.append(element1)
                        compareBadFeature.append(compareElement)
                    else:
                        scatterGood.append(element1)
                        compareGoodFeature.append(compareElement)
                 
                axs.scatter(scatterBad, compareBadFeature, label="Bad Wine")
                axs.scatter(scatterGood, compareGoodFeature, alpha=0.5, label="Good Wine")
                axs.set_xlabel(element)
                axs.set_ylabel(featureToCompare)
                label = "Scatter plot of " + element + " vs "  + featureToCompare
                axs.set_title(label)
                axs.legend()
                figs.show()