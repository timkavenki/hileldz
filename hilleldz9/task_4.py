''''Написати функцію яка замінить у тексті слово на інше.'''
def fake_string(input_string, target_word, new_word, num_replacements):
    words = input_string.split()
    replaced_count = 0
    result = []

    for word in words:
        if word == target_word and replaced_count < num_replacements:
            result.append(new_word)
            replaced_count += 1
        else:
            result.append(word)

    return ' '.join(result)


input_string1 = 'DC makes good movies, DC makes good comics'
result1 = fake_string(input_string1, 'DC', 'Marvel', 1)
print(result1)

input_string2 = 'DC makes good movies, DC makes good comics'
result2 = fake_string(input_string2, 'DC', 'Marvel', 2)
print(result2)