# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_str = 'Неабв сложно выучить стишокабв пайтон'
# print(my_str)
# res = list(filter(lambda item: 'абв' not in item, my_str.split()))
# print(res)

my_str = 'Неабв сложно выучить стишокабв пайтон'
print(my_str)
my_str = my_str.split()
list_1 = [item for item in my_str if'абв' not in item] 
print(list_1)