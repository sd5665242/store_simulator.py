class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products

    def get_product_quantity(self, product):
        return product.quantity

    def set_product_quantity(self, product, quantity):
        product.quantity = quantity

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price * product.quantity
        return total_price

    def get_most_expensive_product(self):
        most_expensive_product = self.products[0]
        for product in self.products:
            if product.price > most_expensive_product.price:
                most_expensive_product = product
        return most_exp
