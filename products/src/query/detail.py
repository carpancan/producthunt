from django.shortcuts import get_object_or_404
from products.models import Product


class Manager:
    __query = None
    __product = None
    __product_output = {}

    def __call__(self, query):
        self.__initialize(query)
        self.__obtain_product()
        self.__format_product_data()
        return self.__product_output

    def __initialize(self, query):
        self.__query = query

    def __obtain_product(self):
        self.__product = get_object_or_404(Product, pk=self.__query.get_product_id())

    def __format_product_data(self):
        try:
            icon = ''
            if self.__product.icon is not None:
                icon = self.__product.icon.url
            image = ''
            if self.__product.image is not None:
                image = self.__product.image.url
        except ValueError as exception:
            icon = ''
            image = ''

        self.__product_output['id'] = self.__product.id
        self.__product_output['title'] = self.__product.title
        self.__product_output['url'] = self.__product.url
        self.__product_output['body'] = self.__product.body
        self.__product_output['icon'] = icon
        self.__product_output['image'] = image
        self.__product_output['rate'] = self.__product.rate
        self.__product_output['hunter'] = self.__product.user.username
        self.__product_output['published'] = self.__product.published_pretty()



class Query:
    __product_id = None

    def __init__(self, product_id):
        self.__product_id = product_id

    def get_product_id(self):
        return self.__product_id
