filename = input("Введіть назву файлу (разом з розширенням, наприклад, text.txt): ")
with open(filename, 'w') as file:
    print("Введіть дані. Для завершення введення лише натисніть Enter.")
    while True:
        data = input()
        if data == "":
            break
        file.write(data + "\n")

print(f"Дані були записані у файл {filename}.")