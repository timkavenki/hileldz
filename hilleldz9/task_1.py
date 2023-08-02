"''Написати функцію, яка рахуватиме кількість очок футбольної команди.'''
def count_points():
    win = int(input("Кількість перемог: "))
    draw = int(input("Кількість нічиїх: "))
    loss = int(input("Кількість поразок: "))

    total_points = (win * 3) + (draw * 1) + (loss * -1)
    return total_points


result = count_points()
print("Загальна кількість очок:", result)