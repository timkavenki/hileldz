'''. Користувач вводить число від 1 до 10, програма генерує рандомне число від 1 до 10,
 якщо числа співпадають надрукувати 'You won!' якщо ні - 'You lose!'. Дати користувачеві три спроби;)'''

import random

random_number = random.randint(1, 10)

attempts = 3

while attempts > 0:
    user_number = int(input("Введіть число від 1 до 10: "))
    if user_number == random_number:
        print("You won!")
        break
    attempts -= 1
    print("You lose!")
if attempts == 0:
    print("Game over!")