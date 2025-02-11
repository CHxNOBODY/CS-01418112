def fn1(a, b):
    count = 0
    while True:
        if a == 0:
            break
        if a % 10 >= b:
            count += 1
        a //= 10
    return count

x = int(input())
y = int(input())

print(fn1(a = x, b = y))