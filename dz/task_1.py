list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

common_numbers = set1 & set2

count = len(common_numbers)

print("Кількість спільних чисел:", count)