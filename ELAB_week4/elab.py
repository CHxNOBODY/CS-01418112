import math

x = float(input("Enter x : "))

ans = 0
if x == 0:
    ans = x
elif x > 0 and x <= 99:
    ans = 3 * (x ** 2) - (1 - x) ** 2
elif x > 99:
    ans = 2 * (x ** 3) - x / math.sqrt(x + 1)
else:
    ans = math.sqrt((x ** 2) + 1)
    
print(f"f({x:.2f}) = {int(math.ceil(ans))}")