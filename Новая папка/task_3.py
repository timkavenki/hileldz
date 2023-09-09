import re

while True:
    password = input("Введіть пароль: ")

    # Перевірка довжини пароля
    if len(password) < 8:
        print("Пароль повинен містити щонайменше 8 символів.")
        continue

    # Перевірка наявності маленьких літер (a-z)
    if not re.search(r'[a-z]', password):
        print("Пароль повинен містити щонайменше одну маленьку літеру (a-z).")
        continue

    # Перевірка наявності великих літер (A-Z)
    if not re.search(r'[A-Z]', password):
        print("Пароль повинен містити щонайменше одну велику літеру (A-Z).")
        continue

    # Перевірка наявності цифр (0-9)
    if not re.search(r'[0-9]', password):
        print("Пароль повинен містити щонайменше одну цифру (0-9).")
        continue

    # Перевірка наявності спеціальних символів ($#@-+=)
    if not re.search(r'[$#@\-+=]', password):
        print("Пароль повинен містити щонайменше один із символів: $#@-+=")
        continue

    print("Пароль відповідає вимогам: Password is correct")
    break