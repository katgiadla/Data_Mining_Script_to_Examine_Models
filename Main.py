import sys

from Entryoffile import check_file
from CSVfileoption import read_convert_csv, print_data
from mapeanalys import calculatePercentageErrors, calculateErrors, calculateMeanError
import ExceptionsClasses as ec

if __name__ == '__main__':
    try:
        check_file()
    except ec.FailureInputException:
        print(ec.FailureInputException.message)
        exit()
    finally:
        print('Data is loaded correct!')
    df = read_convert_csv(sys.argv[1])
    print_data(df)
    print_data(calculateMeanError(calculateErrors(df)))