''''Дано рядок.

  a. Виведіть третій символ цього рядка.

  b. виведіть передостанній символ цього рядка.

  с. виведіть перші п'ять символів цього рядка.

  d. виведіть весь рядок, крім двох останніх символів.

  e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи

  з першого).'''
input_string = input("Введіть рядок: ")

# a. Виведіть третій символ цього рядка.
print("a. Третій символ:", input_string[2])

# b. Виведіть передостанній символ цього рядка.
print("b. Передостанній символ:", input_string[-2])

# c. Виведіть перші п'ять символів цього рядка.
print("c. Перші п'ять символів:", input_string[:5])

# d. Виведіть весь рядок, крім двох останніх символів.
print("d. Весь рядок, крім двох останніх символів:", input_string[:-2])

# e. Виведіть усі символи з парними індексами.
print("e. Символи з парними індексами:", input_string[::2])

# f. Виведіть усі символи з непарними індексами.
print("f. Символи з непарними індексами:", input_string[1::2])

# g. Виведіть усі символи у зворотному порядку.
print("g. Усі символи у зворотному порядку:", input_string[::-1])

# h. Виведіть усі символи рядка через один у зворотному порядку.
print("h. Символи через один у зворотному порядку:", input_string[-1::-2])

# i. Виведіть довжину цього рядка.
print("i. Довжина рядка:", len(input_string))