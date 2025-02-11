n = int(input())

count = 0
i = 0
while i <= n:
    if i % 3 != 0:
        print(i)
        count += 1
    i += 1
print(count)