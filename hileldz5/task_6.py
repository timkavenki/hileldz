''' Написати функцію яка прибере з dict елементи із значеннями None:'''


def remove_none_values(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}
data = {
    'first_color': 'Red',
    'second_color': 'Green',
    'third_color': None
}

result = remove_none_values(data)
print(result)