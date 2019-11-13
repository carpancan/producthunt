from products.models import Product
from products.src.exceptions.CustomExceptions import ProductNotExistsException


class Handler:
    __command = None
    __product = None

    def __call__(self, command):
        self.__initialize(command)
        self.__obtain_product()
        self.__add_vote()

    def __initialize(self, command):
        self.__command = command

    def __obtain_product(self):
        try:
            self.__product = Product.objects.get(id=self.__command.get_product_id())
        except Product.DoesNotExist:
            raise ProductNotExistsException()

    def __add_vote(self):
        self.__product.rate += 1
        self.__product.save()


class Command:
    __product_id = None

    def __init__(self, product_id):
        self.__product_id = product_id

    def get_product_id(self):
        return self.__product_id
