class Error(Exception):
    pass

class FailureFileException(Error):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        print(self.message)