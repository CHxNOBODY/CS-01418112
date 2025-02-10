def find_prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

num = int(input("Enter positive integer: "))

if num <= 0:
    print("Invalid number.")
elif num == 1:
    pass
else:
    factors = find_prime_factors(num)
    for factor in factors:
        print(factor)