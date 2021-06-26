class OperationTypeException(Exception):
    def __init__(self, message="Operation type should be +, –, /, * or 0."):
        super().__init__(message)
