class ErrEntityNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)


class ErrEntityConflict(Exception):
    def __init__(self, message):
        super().__init__(message)


class ErrUnAuthorized(Exception):
    def __init__(self, message):
        super().__init__(message)
