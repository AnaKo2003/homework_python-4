# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите k: '))
coefficient = list()
for i in range(1, k + 2):
    coefficient.append(randint(1, 100))

ans = list()
for i in range(len(coefficient)):
    if k == 1:
        ans.append(f'{coefficient[i]}*x')
    elif k == 0:
        ans.append(f'{coefficient[i]}')
    else:
        ans.append(f'{coefficient[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        ans.append('+')
    elif flag == 0:
        ans.append('-')
    k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(ans))
fout.close()