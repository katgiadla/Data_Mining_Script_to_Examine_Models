class ExceptionClasses(Exception):
    pass

class FailureFileException(ExceptionClasses):

    def __init__(self, message: str):
        self.message = message