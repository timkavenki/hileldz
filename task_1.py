import csv

# Клас Product для представлення продукту (кава, чай або додатковий продукт)
class Product:
    def __init__(self, name, product_type, price):
        if product_type not in ['coffee', 'tea', 'additional']:
            raise ValueError("Тип може бути тільки 'coffee', 'tea' або 'additional'.")
        self.name = name
        self.product_type = product_type
        self.price = price

    def __str__(self):
        return f"{self.product_type.capitalize()}: {self.name}, ціна: {self.price}грн."

# Клас Store для управління кавовим магазином
class Store:
    def __init__(self):
        self.products = []

    # Метод для імпорту продуктів з файлу inventory.csv
    def import_products(self, filename="inventory.csv"):
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['Name']
                    product_type = row['Type']
                    price = float(row['Price'])
                    quantity = int(row.get('Quantity', 5))  # За замовчуванням 5 штук кожного продукту
                    for _ in range(quantity):
                        self.products.append(Product(name, product_type, price))
            print("Продукти імпортовані успішно.")
        except FileNotFoundError:
            print("Файл інвентарю не знайдено.")

    # Метод для отримання списку продуктів заданого типу (tea, coffee або всі)
    def get_products(self, product_type='all'):
        if product_type == 'all':
            return self.products
        return [product for product in self.products if product.product_type == product_type]

    # Метод для підрахунку загальної вартості продуктів
    def calculate_total_price(self):
        return sum(product.price for product in self.products)

    # Метод для продажу продукту
    def sell_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return product
        return None

# Приклад використання:
if __name__ == "__main__":
    # Створення магазину
    coffee_shop = Store()

    # Імпорт продуктів з файлу inventory.csv
    coffee_shop.import_products()

    # Отримання списку всіх продуктів
    all_products = coffee_shop.get_products()
    for product in all_products:
        print(product)

    # Отримання списку продуктів типу "coffee"
    coffee_products = coffee_shop.get_products('coffee')
    for product in coffee_products:
        print(product)

    # Підрахунок загальної вартості продуктів
    total_price = coffee_shop.calculate_total_price()
    print(f"Загальна вартість продуктів: {total_price}грн.")

    # Продаж продукту
    sold_product = coffee_shop.sell_product("Еспресо")
    if sold_product:
        print(f"Продано продукт: {sold_product}")
    else:
        print("Продукт не знайдено.")