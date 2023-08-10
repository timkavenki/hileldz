def shift_list(lst, n):
    if n < 0:
        n = -n
        n %= len(lst)
        shifted_list = lst[n:] + lst[:n]
    else:
        n %= len(lst)
        shifted_list = lst[-n:] + lst[:-n]
    return shifted_list

# Приклад використання
input_list = [1, 2, 3, 4, 5]
shift_amount = int(input("Введіть кількість позицій для зсуву: "))
shifted_result = shift_list(input_list, shift_amount)
print("Зсунутий список:", shifted_result)