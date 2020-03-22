class BaseException(Exception):
    def hint(self):
        return "Unknown Error."


class UnknownDateError(BaseException):
    def hint(self):
        return "gcplogs doesn't chosen date."
