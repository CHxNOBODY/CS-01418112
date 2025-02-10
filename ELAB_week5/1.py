n = int(input())

if n <= 0:
    print("ERROR")
else:
    while n > 0:
        print(n % 10)
    n = n // 10
    

    