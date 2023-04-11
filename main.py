
#Задача 10
"""
n = int(input('Введите количество моет: '))
count_eagle = 0
count_tails = 0
for i in range(n):
    x = int(input(f'Положение {i} - й монеты 0 или 1: '))
    if x == 0:
        count_eagle += 1
    else:
        if x != 1:
            print('Значение введено отличное от 0, значит считаем что 1')
            count_tails += 1
        else:
            count_tails += 1
if count_tails > count_eagle:
    print('Перевернуть "Орлов": ' + str(count_eagle))
else:
    print('Перевернуть "Решек": ' + str(count_tails))

#Задача 12

s = int(input('Введите сумму S: '))
p = int(input('Введите произведение P: '))
for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print('Загаданные числа X и Y: ')
            print(i, j)
            break

# Задача 14
"""
n = int(input())
i = 0
    while 2 ** i <= n:
        print(2 ** i)
        i += 1
"""