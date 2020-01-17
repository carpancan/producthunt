class UrlExistsException(Exception):
    __message = None
    __code = None

    def __init__(self, message=None, code=400):
        if message is None:
            message = 'Url already exists'
        self.__message = message
        self.__code = code

    def get_error_code(self):
        return self.__code

    def get_message(self):
        return self.__message


class ProductNotExistsException(Exception):
    __message = None
    __code = None

    def __init__(self, message=None, code=400):
        if message is None:
            message = 'Product not exists'
        self.__message = message
        self.__code = code

    def get_error_code(self):
        return self.__code

    def get_message(self):
        return self.__message