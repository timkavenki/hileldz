'''Програма запитує введення послідовності цілих невід'ємних чисел, доки не буде введено 0. Як тільки

буде введено 0 (нуль), програма повинна порахувати та вивести на екран:'''

numbers = []
while True:
    num = int(input("Введіть число (або 0, щоб завершити): "))
    if num == 0:
        break
    numbers.append(num)

count = len(numbers)
sum_numbers = sum(numbers)
product = 1
max_value = max(numbers)
second_max = sorted(numbers, reverse=True)[1]
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = count - even_count
same_as_max = sum(1 for num in numbers if num == max_value)

average = sum_numbers / count

print("Кількість чисел:", count)
print("Сума чисел:", sum_numbers)
print("Добуток чисел:", product)
print("Середнє арифметичне:", average)
print("Найбільше число:", max_value)
print("Порядковий номер найбільшого числа:", numbers.index(max_value) + 1)
print("Кількість парних чисел:", even_count)
print("Кількість непарних чисел:", odd_count)
print("Друге за величиною число:", second_max)
print("Кількість чисел, рівних найбільшому:", same_as_max)