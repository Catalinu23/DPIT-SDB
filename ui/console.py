from exception.exceptions import ProgramError
from service.product_service import ProductService

class ConsoleUI:
    def __init__(self, product_service: ProductService):
        self.__product_service = product_service

    def __print_menu(self):
        print("1. Admin menu")
        print("2. User menu")
        print("0. Stop")

    def __print_admin_menu(self):
        print("1. View all products")
        print("2. Add product")
        print("3. Remove product")
        print("4. Modify a product")
        print("5. View all products from a brand")
        print("0. Exit admin mode")

    def __print_user_menu(self):
        print("1. View all products")
        print("2. Buy product")
        print("3. View all products in budget")
        print("0. Exit user mode")

    def __add_product(self):
        code = input("Code: ")
        name = input("Name: ")
        brand = input("Brand: ")
        price = int(input("Price: "))
        amount = int(input("Amount: "))
        self.__product_service.add(code, name, brand, price, amount)

    def __print_product(self, product):
        print("Code: " + product.get_code())
        print("Name: " + product.get_name())
        print("Brand: " + product.get_brand())
        print("Price: " + str(product.get_price()))
        print("Amount: " + str(product.get_amount()))
        print("---------------------------")

    def __remove_product(self):
        code = input("Code: ")
        self.__product_service.delete(code)

    def __get_product_by_code(self):
        code = input("Code: ")
        print(self.__product_service.find_by_code(code))

    def __edit_product(self):
        code = input("Code: ")
        name = input("New name: ")
        brand = input("New brand: ")
        price = int(input("New price: "))
        amount = int(input("New amount: "))
        self.__product_service.edit(code, name, brand, price, amount)

    def __get_all_products(self):
        for product in self.__product_service.get_repo().get_all():
            self.__print_product(product)

    def __get_products_by_brand(self):
        brand = input("Brand: ")
        products = self.__product_service.get_products_by_brand(brand)
        for product in products:
            self.__print_product(product)

    def __get_products_in_budget(self):
        budget = int(input("Budget: "))
        products = self.__product_service.get_products_in_budget(budget)
        if products is not None:
            for product in products:
                self.__print_product(product)
        else:
            print("No products in budget!")

    def __buy_product(self):
        code = input("Code: ")
        amount = int(input("Amount: "))
        self.__product_service.buy_product(code, amount)

    def run(self):
        while True:
            self.__print_menu()
            admin_mode = False
            try:
                command = int(input("Choose the command: ").strip())
                if command == 0:
                    return
                elif command == 1:
                    admin_mode = True
                elif command == 2:
                    admin_mode = False
            except ProgramError as error:
                print(error)

            if admin_mode:
                while True:
                    self.__print_admin_menu()
                    try:
                        command = int(input("Choose the command: ").strip())
                        if command == 0:
                            break
                        elif command == 1:
                            self.__get_all_products()
                        elif command == 2:
                            self.__add_product()
                        elif command == 3:
                            self.__remove_product()
                        elif command == 4:
                            self.__edit_product()
                        elif command == 5:
                            self.__get_products_by_brand()
                    except ProgramError as error:
                        print(error)
            else:
                while True:
                    try:
                        self.__print_user_menu()
                        command = int(input("Choose the command: ").strip())
                        if command == 0:
                            break
                        elif command == 1:
                            self.__get_all_products()
                        elif command == 2:
                            self.__buy_product()
                        elif command == 3:
                            self.__get_products_in_budget()
                    except ProgramError as error:
                        print(error)



