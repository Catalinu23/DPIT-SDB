class Repository:
    def __init__(self):
        self.__entities_list = []

    def __find_position(self, entity):
        for i in range(len(self.__entities_list)):
            if self.__entities_list[i] == entity:
                return i
        return None

    def find_by_code(self, code):
        for i in range(len(self.__entities_list)):
            #print(self.__entities_list[i].get_name())
            if self.__entities_list[i].get_code() == code:
                # print(self.__entities_list[i].get_name())
                return self.__entities_list[i]

    def buy_product(self, code, amount):
        entity = self.find_by_code(code)
        if entity is None:
            print("Product does not exist!")
            return
        position = self.__find_position(entity)
        if self.__entities_list[position].get_amount() < amount:
            print("Not enough items!")
            return
        self.__entities_list[position].set_amount(self.__entities_list[position].get_amount() - int(amount))
        print("Product bought succesfully!")

    def edit(self, code, name, brand, price, amount):
        entity = self.find_by_code(code)
        if entity is None:
            print("Product does not exist!")
            return
        self.__entities_list[self.__find_position(entity)].set_name(name)
        self.__entities_list[self.__find_position(entity)].set_brand(brand)
        self.__entities_list[self.__find_position(entity)].set_price(price)
        self.__entities_list[self.__find_position(entity)].set_amount(amount)

    def add(self, new_entity):
        if self.__find_position(new_entity) is not None:
            print("Product already exists!")
            return
        self.__entities_list.append(new_entity)

    def delete(self, entity):
        position = self.__find_position(entity)
        if position is None:
            print("Product does not exist!")
            return
        del self.__entities_list[position]

    def get_products_by_brand(self, brand):
        branded_products = []
        for entity in self.__entities_list:
            if entity.get_brand() == brand:
                branded_products.append(entity)
        return branded_products

    def get_products_in_budget(self, budget):
        products = []
        for entity in self.__entities_list:
            if entity.get_price() <= budget:
                products.append(entity)
        return products

    def get_all(self):
        return self.__entities_list
