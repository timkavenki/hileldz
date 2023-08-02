def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

temperature = float(input("Введіть температуру: "))
temperature_type = input("Введіть тип температури (C, F, K): ")

if temperature_type == 'C':
    celsius = temperature
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
elif temperature_type == 'F':
    fahrenheit = temperature
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = fahrenheit_to_kelvin(fahrenheit)
elif temperature_type == 'K':
    kelvin = temperature
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = kelvin_to_fahrenheit(kelvin)
else:
    print("Непідтримуваний тип температури")

print("Температура у Цельсіях:", celsius)
print("Температура у Фарренгейтах:", fahrenheit)
print("Температура у Кельвінах:", kelvin)