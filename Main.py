import sys

from Entryoffile import check_file
from CSVfileoption import read_convert_csv, print_data
from mapeanalys import calculatePercentageErrors, calculateErrors, calculateMeanError
from ExceptionsClasses import FailureInputException

if __name__ == '__main__':
    try:
        check_file()
    except FailureInputException:
        print(FailureInputException.message)
        exit()
    finally:
        print('Data is loaded correct!')
    df = read_convert_csv(sys.argv[1])
    print_data(df)
    print_data(calculateMeanError(calculateErrors(df)))