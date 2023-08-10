'''* Даний список чисел. Визначте, скільки в цьому списку елементів, які більше двох своїх сусідів (ліворуч і праворуч),

та виведіть кількість таких елементів. Крайні елементи списку ніколи не враховуються, оскільки вони мають недостатньо

сусідів.'''
def count_elements_with_greater_neighbors(nums):
    count = 0
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            count += 1
    return count

numbers = [int(x) for x in input("Введіть список чисел через пробіл: ").split()]

result = count_elements_with_greater_neighbors(numbers)
print(f"Кількість елементів, які більше своїх сусідів: {result}")