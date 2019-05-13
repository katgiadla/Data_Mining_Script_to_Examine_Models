import pandas as pd
import numpy as np

def calculateError(CSVFile: pd.DataFrame):
    errorTab = np.zeros((len(CSVFile), 1))
    for i in range(0, len(CSVFile)):
        errorTab[i] = float(CSVFile.iloc[i]['Model'] - CSVFile.iloc[i]['DaneRealne'])
    return errorTab