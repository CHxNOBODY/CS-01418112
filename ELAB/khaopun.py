import math

n = int(input())
sym = str(input())
sym2 = str(input())

n_use = int(n//2+1)

print(*n_use*(sym), sep=sym2)
