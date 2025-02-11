n = int(input())

i = 0 
count  = 0
while i <= n:
    if i % 3 != 0:
        count += 1
    i += 1
print(count)