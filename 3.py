num = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 8, 8]
list = []
for i in num:
    if num.count(i) == 1:
        list.append(i)
print(list)