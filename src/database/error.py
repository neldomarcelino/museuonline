class ErrorDatabase(Exception):

    def __init__(self,message):
        self.message = message


class syntaxError(ErrorDatabase):
    pass


class connectionError(ErrorDatabase):
    pass