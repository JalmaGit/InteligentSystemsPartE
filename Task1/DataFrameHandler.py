import pandas as pd

class DataFrameHandler:

    def __init__(self, fileName) -> None:
        self.dataFrame = pd.read_csv(fileName)
        self.dataFrame = DataFrameHandler(self.dataFrame)

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