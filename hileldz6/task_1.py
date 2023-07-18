'''Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:

  Input:

    coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
    code = ('BTC', 'ETH', 'XRP', 'LTC')'''

def combine_tuples_to_dict(coin, code):
    return dict(zip(coin, code))

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

result = combine_tuples_to_dict(coin, code)
print(result)