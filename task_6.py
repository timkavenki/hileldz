x = float(input("Введіть число: "))

numbers = (10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0)

if x in numbers or -x in numbers:
    print("x є у списку.")
else:
    print("x не є у списку.")