import os
import sys
from csvfileoptions import read_convert_csv, print_data

def check_file():
    if (sys.argv).__len__() != 2:
        return False
    else:
        return True

if __name__ == '__main__':
    if (check_file() == False):
        print("Too much or not much")
        exit()
    df = read_convert_csv(sys.argv[1])
    print(df)