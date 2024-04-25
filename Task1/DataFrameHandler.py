import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataFrameHandler:

    def __init__(self, fileName):
        self.dataFrame = pd.read_csv(fileName)
        self.dataFrame = self.dataFrame.drop_duplicates()
        self.dataFrame = self.dataFrame.dropna(axis=0, how='all')
        self.dataFrame = self.dataFrame.dropna(axis=1, how='any')

        print(self.dataFrame.describe())

    def printObjectsPerClass(self, feature):
        objectsBelongingToEachClass = np.empty(0)

        labels = np.array(["Disgusting","Extremly Bad", "Very Bad", "Bad", "Kinda Bad", "Mediocre", "Decent", "Good", "Very Good", "Extremely Good", "Perfect"])

        for i in range(max(self.dataFrame[feature]+3)):
            objectsBelongingToEachClass = np.append(objectsBelongingToEachClass,(self.dataFrame[feature] == i).sum())
            print("When quality is",i,", the number of wines with said quality is:",(self.dataFrame[feature] == i).sum(),labels[i])

    def printSingleHistogram(self, feature, binLimit: bool = False):
        columnData = self.dataFrame[feature]

        fig, ax = plt.subplots()

        if feature == "quality":
            customBins = np.arange(11)
            ax.hist(columnData, customBins)
        elif binLimit:
            customBins = np.arange(np.min(self.dataFrame[feature]),np.max(self.dataFrame[feature]+1),1)
            ax.hist(columnData, customBins)
        else:
            ax.hist(columnData)

        fig.show()
