'''. Написати функцію, яка повертає поточний час. І обернути її у декоратор

  який відрахує 3 секунди.'''

import time

def countdown_decorator(func):
    def wrapper():
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        return func()
    return wrapper

@countdown_decorator
def get_current_time():
    current_time = time.strftime('%H:%M')
    return current_time

print(get_current_time())

