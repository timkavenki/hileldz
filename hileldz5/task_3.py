'''Написати функцію яка поверне площу фігури: за замовчуванням трикутника, опціонально квадрату.
 На вході 2 величини та параметр типу фігури.'''

def calculate_area(a, b, shape='triangle'):
    if shape == 'triangle':
        return 0.5 * a * b
    elif shape == 'square':
        return a * b
    else:
        raise ValueError("Невідомий тип фігури. Підтримуються лише 'triangle' та 'square'.")

a = 5
b = 8

triangle_area = calculate_area(a, b, shape='triangle')
print(f"Площа трикутника зі сторонами {a} і {b}: {triangle_area}")

square_area = calculate_area(a, b, shape='square')
print(f"Площа квадрата зі сторонами {a} і {b}: {square_area}")