import math

d = input("Задайте число: ")
p = float(input("Задайте число для вычисления: "))
countL = 0
countR = 0
for i in str(d):
    if i != '.':
        countL += 1
    else:
        break
for i in str(d):
    countR += 1
T= countR - countL - 1

print(round(p, T))