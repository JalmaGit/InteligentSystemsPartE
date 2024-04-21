import pandas as pd
import DataFrameHandler as DFH

fileName = "used_cars_data.csv"

dfh = DFH.DataFrameHandler(fileName)

dataFrame = dfh.dataFrame

print(dataFrame.describe())