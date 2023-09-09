import re

def format_phone_number(phone_number):
    # Видаляємо всі символи, окрім цифр та '+'
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)

    # Перевіряємо, чи номер відповідає одному з припустимих форматів
    if re.match(r'(\+?38)?\d{10}$', cleaned_number):
        # Додаємо код країни, якщо його немає
        if not cleaned_number.startswith('+38'):
            cleaned_number = '+38' + cleaned_number
        # Форматуємо номер у вигляді (+38) 063 999-99-99
        formatted_number = re.sub(r'(\+38)(\d{3})(\d{3})(\d{2})(\d{2})', r'(\1) \2 \3-\4-\5', cleaned_number)
        return formatted_number
    else:
        return 'Failed to recognize number'

input_number = input("Введіть номер телефону: ")
formatted_number = format_phone_number(input_number)
print(f"Результат форматування: {formatted_number}")