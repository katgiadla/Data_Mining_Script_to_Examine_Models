import sys
import ExceptionsClasses as ec

def check_file():
    if (sys.argv).__len__() != 2:
        raise ec.FailureFileException('File is not found!')
    else:
        pass
    return