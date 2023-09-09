import random
from tabulate import tabulate

# Клас для представлення будинку
class House:
    def __init__(self):
        self.population = random.randint(1, 100)

# Клас для представлення вулиці з будинками
class Street:
    def __init__(self, number):
        self.number = number
        self.houses = [House() for _ in range(random.randint(5, 20))]

# Клас для представлення міста
class City:
    def __init__(self, name):
        self.name = name
        self.streets = [Street(i + 1) for i in range(random.randint(2, 5))]

    def get_population(self):
        return sum(house.population for street in self.streets for house in street.houses)

    def print_city_table(self):
        table_data = []
        for street in self.streets:
            for i, house in enumerate(street.houses, start=1):
                table_data.append([street.number, i, house.population])

        table_headers = ["Вулиця", "Будинок", "Населення"]
        print(tabulate(table_data, headers=table_headers))

# Створення міста і його заповнення будинками
my_city = City("Моє місто")

# Отримання та виведення загальної кількості населення міста
population = my_city.get_population()
print(f"Загальна кількість населення у місті {my_city.name}: {population} осіб")

# Виведення таблиці міста
print("\nТаблиця міста:")
my_city.print_city_table()