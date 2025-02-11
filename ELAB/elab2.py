a = float(input("Enter buying amount: "))

ans = a
if a >= 1000 and a < 3000:
    ans = a - (a * 0.1)
elif a >= 3000:
    ans = a - (a * 0.15)
    
print(f'Amount due after discount is {ans:.2f} baht.')
