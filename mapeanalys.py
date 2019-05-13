import pandas as pd
import numpy as np

def calculateError(CSVFile: pd.DataFrame):
    errorTab = np.zeros((len(CSVFile), 1))
    for i in range(0, len(CSVFile)):
        errorTab[i] = float(CSVFile.iloc[i]['RealData'] - CSVFile.iloc[i]['Model'])
    return errorTab