'''Написати функцію яка поверне найдовше слово у рядку:'''
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = "I love big candies"
result = longest_word(sentence)
print(result)