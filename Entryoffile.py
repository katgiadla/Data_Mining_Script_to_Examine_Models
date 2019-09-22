import sys
from ExceptionsClasses import FailureInputException

def check_file():
    if (sys.argv).__len__() != 2:
        raise FailureInputException('Too much or too such file')
    else:
        pass
    return