def is_palindrome(text):
    # Видаляємо з тексту всі неалфавітні символи та перетворюємо на нижній регістр
    cleaned_text = ''.join(filter(str.isalpha, text)).lower()

    # Порівнюємо текст з його реверсом
    return cleaned_text == cleaned_text[::-1]


text = input("Введіть текст: ")
if is_palindrome(text):
    print("Це паліндром!")
else:
    print("Це не паліндром.")