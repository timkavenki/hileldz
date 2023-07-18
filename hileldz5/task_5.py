'''Написати функцію square, що приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):
периметр квадрата, площа квадрата та діагональ квадрата.'''

import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side

    return perimeter, area, diagonal
side = 5
result = square(side)
print("Периметр:", result[0])
print("Площа:", result[1])
print("Діагональ:", result[2])