from domain.product import Product
from repository.repository import Repository

class ProductService:
    def __init__(self, admin_repository: Repository):
        self.__product_repository = admin_repository

    def get_repo(self):
        return self.__product_repository

    def add(self, code, name, brand, price, amount):
        self.__product_repository.add(Product(code, name, brand, price, amount))

    def find_by_code(self, code):
        return self.__product_repository.find_by_code(code)

    def delete(self, code):
        self.__product_repository.delete(self.find_by_code(code))

    def edit(self, code, name, brand, price, amount):
        self.__product_repository.edit(code, name, brand, price, amount)

    def get_products_by_brand(self, brand):
        return self.__product_repository.get_products_by_brand(brand)

    def buy_product(self, code, amount):
        self.__product_repository.buy_product(code, amount)

    def get_products_in_budget(self, budget):
        return self.__product_repository.get_products_in_budget(budget)
