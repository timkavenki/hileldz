
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{id(self)} | Product name: {self.name} | price: {self.price}'


class VIPProduct(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        discount = self.price * 0.2
        self.price -= discount
        self.name = f'{self.name}_discount'


class User:
    info = 'AWESOME USER!'

    def __init__(self, name):
        self._name = name
        self.cart = Cart()

    @property
    def name(self):
        return self._name

    def checkout(self):
        return self.cart.checkout()

    def __repr__(self):
        return f'User: {self.name} with {self.cart}'


class Cart:
    def __init__(self):
        self.products = []

    def __repr__(self):
        return '\n'.join([str(p) for p in self.products])

    def add(self, product: Product):
        self.products.append(product)

    def remove(self, product: Product):
        if product in self.products:
            self.products.pop(self.products.index(product))
    def checkout(self):
        return sum(product.price for product in self.products)

    def clean(self):
        self.products.clear()
print(User('alan').name)

# Client code:
first_user = User('yosik')
first_user.cart.add(Product('Duru soap', 15.50))
first_user.cart.add(Product('Duru soap', 11.50))
first_user.cart.add(Product('Duru soap', 17.50))
first_user.cart.add(Product('Duru soap', 13.50))
first_user.cart.add(Product('Duru soap', 13.50))
first_user.cart.add(VIPProduct('Duru soap', 13.50))
print(first_user.cart)
print(first_user.checkout())
