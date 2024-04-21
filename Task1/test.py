import pandas as pd
import numpy as np

def dataFrameReplacer(df, replaceList):

    for name in replaceList: 

        checkerDict = {}

        featureValue = 0
        for i in df[name]:
            if i not in checkerDict:
                checkerDict[i] = featureValue
                featureValue += 1.0

        for key, value in checkerDict.items():
            df.loc[df[name] == key, name] = float(value)
        
        df[name] = df[name].replace("None", float('nan'))
        df[name] = df[name].astype('float64')

    return df

fileName = "used_cars_data.csv"

dataFrame = pd.read_csv(fileName)

namesToReplace = ["brand", "model","engine","fuel","gearbox","location"]

newDataFrame = dataFrameReplacer(dataFrame, namesToReplace)

print(newDataFrame["gearbox"])
print(newDataFrame.describe())