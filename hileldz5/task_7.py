'''** дод. Написати функцію `is_date`, що приймає 3 аргументи - день, місяць і рік.
Повернути `True`, якщо дата коректна (треба враховувати число місяця.
Наприклад 30.02 - дата не коректна, так само 31.06 або 32.07 тощо), та `False` інакше.'''

import datetime

def is_date(day, month, year):
    try:
        date_string = f"{year}-{month}-{day}"
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

day = 30
month = 2
year = 2023

if is_date(day, month, year):
    print("Дата є коректною.")
else:
    print("Дата є некоректною.")