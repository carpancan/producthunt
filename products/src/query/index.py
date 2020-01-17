from django.db.models.functions import Coalesce, Lower

from products.models import Product


class Manager:
    __query = None
    __products = None
    __products_output = []

    def __call__(self, query):
        self.__initialize(query)
        self.__obtain_products()
        self.__format_product_output()

        return self.__products_output

    def __initialize(self, query):
        self.__query = query

    def __obtain_products(self):
        self.__products = Product.objects.order_by('rate').all().reverse()

    def __format_product_output(self):
        self.__products_output.clear()
        for product in self.__products:
            icon, image = self.__obtain_medias_url(product)
            formatted_product = {
                    'id': product.id,
                    'title': product.title,
                    'url': product.url,
                    'summary': product.summary(),
                    'icon': icon,
                    'image': image,
                    'rate': product.rate,
                    'hunter': product.user.username,
                    'published': product.published_pretty(),
                }
            self.__products_output.append(formatted_product)

    def __obtain_medias_url(self, product):
        try:
            icon = ''
            if product.icon is not None:
                icon = product.icon.url
            image = ''
            if product.image is not None:
                image = product.image.url
        except ValueError:
            icon = ''
            image = ''

        return icon, image


class Query:
    __user_id = None

    def __init__(self, user_id=None):
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id
