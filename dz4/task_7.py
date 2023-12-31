'''** Дано два списки чисел. Надрукувати:

  - числа, що містяться одночасно як у першому списку, так і в другому

  - числа, що містяться в першому, але відсутні в другому

  - тільки унікальні для першого та другого списків'''
def main():
    list1 = [int(x) for x in input("Введіть перший список чисел через пробіл: ").split()]
    list2 = [int(x) for x in input("Введіть другий список чисел через пробіл: ").split()]

    common_elements = list(set(list1) & set(list2))
    unique_to_list1 = list(set(list1) - set(list2))
    unique_to_list2 = list(set(list2) - set(list1))

    print("Числа, що містяться одночасно в обох списках:", common_elements)
    print("Числа, що містяться в першому списку, але відсутні в другому:", unique_to_list1)
    print("Числа, що містяться в другому списку, але відсутні в першому:", unique_to_list2)

if __name__ == "__main__":
    main()