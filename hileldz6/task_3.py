''' Дано перелік значень. Повернути словник, де кожен ключ - це індекс листа,

  а значення листа – це значення ключа:

  Input:'''

def list_to_dict(lst):
    return {index: value for index, value in enumerate(lst)}

input_list = ['a', 'b', 'c', 'd', 'e']
result_dict = list_to_dict(input_list)
print(result_dict)