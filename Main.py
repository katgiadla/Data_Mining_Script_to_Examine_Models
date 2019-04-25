import os
import sys
from csvfileoptions import read_convert_csv, print_data

if __name__ == '__main__':
    df = read_convert_csv('testFile.csv')
    print(df)