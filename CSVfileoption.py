import pandas as pd

def read_convert_csv(pathtofile: str):
    df = pd.read_csv(pathtofile,
                     names=['DaneRealne', 'Model'],
                     dtype={'DaneReal': float, 'Model': float})
    return df

def print_data(mydata: pd.DataFrame):
    print(mydata)
    return