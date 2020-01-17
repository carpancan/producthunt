from datetime import timezone

from django.utils import timezone

from products.models import Product
from products.src.exceptions import custom_exceptions


class Handler:
    __command = None

    def __call__(self, command):
        self.__initialize(command)
        self.__check_if_url_exists()
        return self.__create_product()

    def __initialize(self, command):
        self.__command = command

    def __check_if_url_exists(self):
        try:
            Product.objects.get(url=self.__command.get_url())
            raise custom_exceptions.UrlExistsException('Url already in use')
        except Product.DoesNotExist as exception:
            return False

    def __create_product(self):
        new_product = Product(
            title=self.__command.get_title(),
            url=self.__command.get_url(),
            body=self.__command.get_body(),
            icon=self.__command.get_icon(),
            image=self.__command.get_image(),
            published=timezone.datetime.now(),
            user=self.__command.get_user()
        )
        new_product.save()


class Command:
    __title = __url = __body = __icon = __image = __user = None

    def __init__(self, title, url, body, icon, image, user):
        self.__title = title
        self.__url = url
        self.__body = body
        self.__icon = icon
        self.__image = image
        self.__user = user

    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_body(self):
        return self.__body

    def get_icon(self):
        return self.__icon

    def get_image(self):
        return self.__image

    def get_user(self):
        return self.__user
