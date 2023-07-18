''''1. Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000,
і повертає `True`, якщо воно просте, і `False` - інакше.'''

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
number = 73
if is_prime(number):
    print(f"{number} є простим числом")
else:
    print(f"{number} не є простим числом")