import sys

from Entryoffile import check_file
from CSVfileoption import read_convert_csv, print_data
from mapeanalys import calculateError

if __name__ == '__main__':
    if (check_file() == False):
        print("Too much or not much arguments")
        exit()
    df = read_convert_csv(sys.argv[1])
    print_data(df)
    print_data(calculateError(df))