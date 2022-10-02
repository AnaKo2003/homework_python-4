N = int(input("Задайте число:"))

def multiplier(n):
    result = list()
    d = 2
    while d<= n:
        if n % d == 0:
            result.append(d)
            n = n/d
        else:
            d += 1
    return result

print(multiplier(N))