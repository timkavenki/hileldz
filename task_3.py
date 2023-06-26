v = int(input("Введіть швидкість Васі: "))
t = int(input("Введіть час у годинах: "))

distance = v * t

if v > 0:
    position = distance % 100
else:
    position = 100 - (abs(distance) % 100)

if position != 0:
    print("Вася зупиниться на відмітці", position)
else:
    print("Вася зупиниться на початковій відмітці")

