# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.



count = 1
with open('file_4_1.txt', 'r') as data:
    my_data = data.read()
    print(my_data)

prev = 'first'
coef = str
res = ''

for item in my_data:
    if prev == 'first':
        prev = item
    else:
        if item == prev:
            count += 1
        else:
            coef = str(count)
            res += coef + prev
            prev = item
            count = 1
print(res)

data_1 = open('file_4_2.txt', 'a')
data_1.write(res)
data_1.close()

