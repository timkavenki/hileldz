import re

def is_valid_ua_license_plate(plate):
    # Заміна букв 'I' на 'І' та 'A' на 'А' для українських літер
    plate = plate.upper().replace('I', 'І').replace('A', 'А')

    # Регулярний вираз для валідації автомобільних номерів
    pattern_2004 = re.compile(r'^[А-ЯІ]{2}\d{4}[А-ЯІ]{2}$')
    pattern_2013 = re.compile(r'^[А-ЯІ]{2}\d{4}[А-ЯІ]{1}\d{2}$')

    if pattern_2013.match(plate):
        return "2013 рік (новий формат)"
    elif pattern_2004.match(plate):
        return "2004 рік (старий формат)"
    else:
        return "Не є валідним номером"

# Приклади використання:
input_plate = input("Введіть номер автомобільного номера: ")
result = is_valid_ua_license_plate(input_plate)
print(f"Результат перевірки: {result}")