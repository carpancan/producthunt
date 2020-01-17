from django.contrib.auth.models import User
from .exceptions import CustomExceptions


class Register:
    __new_user_dto = None

    def create_user(self, new_user_dto):
        self.__initialize(new_user_dto)
        self.__check_if_user_exists()
        return self.__persist_user()

    def __initialize(self, new_user_dto):
        self.__new_user_dto = new_user_dto

    def __check_if_user_exists(self):
        try:
            User.objects.get(username=self.__new_user_dto.get_username())
            raise CustomExceptions.UserExistsException('User already in use')
        except User.DoesNotExist as exception:
            return False

    def __persist_user(self):
        return User.objects.create_user(
            username=self.__new_user_dto.get_username(),
            password=self.__new_user_dto.get_password()
        )


class NewUserDto:
    __register_data = None

    def __init__(self, request):
        self.__initialize(request)

    def __initialize(self, request):
        self.__register_data = self.__prepare_register_data(request)

    def __prepare_register_data(self, request):
        data = {}
        for item, value in request.items():
            if 'csrfmiddlewaretoken' in item:
                continue

            data[item] = value

        return data

    def get_username(self):
        return self.__register_data.get('username')

    def get_password(self):
        return self.__register_data.get('password')

    def get_password_confirm(self):
        return self.__register_data.get('password_confirm')
