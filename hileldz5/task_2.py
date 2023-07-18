"""2. Написати програму яка поверне кількість введених користувачем слів та загальну кількість символів."""

def count_words_and_characters():
    text = input("Введіть текст: ")
    words = text.split()
    word_count = len(words)
    character_count = len(text)

    return word_count, character_count

word_count, character_count = count_words_and_characters()

print("Кількість слів:", word_count)
print("Загальна кількість символів:", character_count)