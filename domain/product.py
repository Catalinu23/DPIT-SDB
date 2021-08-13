class Product:
    def __init__(self, code, name, brand, price, amount):
        self.__code = code
        self.__name = name
        self.__brand = brand
        self.__amount = amount
        self.__price = price

    def get_code(self):
        return self.__code

    def set_code(self, new_code):
        self.__code = new_code

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def get_amount(self):
        return self.__amount

    def set_amount(self, new_amount):
        self.__amount = new_amount

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
