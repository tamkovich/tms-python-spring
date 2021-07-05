class ChoiceException(Exception):
    def __init__(self, message='Выберите +, -, * либо / '):
        super().__init__(message)
