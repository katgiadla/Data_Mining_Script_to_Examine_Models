import pandas as pd
import numpy as np

def calculateErrors(CSVFile: pd.DataFrame):
    errorTab = np.zeros((len(CSVFile), 1))
    for i in range(0, len(CSVFile)):
        errorTab[i] = float(CSVFile.iloc[i]['RealData'] - CSVFile.iloc[i]['Model'])
    return errorTab

def calculatePercentageErrors(CSVFile: pd.DataFrame, errorsTab: np.ndarray):
    percentageErrorsTab = np.zeros((len(CSVFile), 1))
    for i in range(0, len(CSVFile)):
        percentageErrorsTab[i] = (errorsTab[i]/CSVFile.iloc[i]['RealData'])*100
    return percentageErrorsTab