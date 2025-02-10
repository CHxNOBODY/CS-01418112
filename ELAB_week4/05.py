age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
nit = 0
valid = True
if age not in range(15,61):
    print("Invalid age.")
    valid = False
elif income not in range(1,80000):
    print("Invalid income.")
    valid = False
elif income in range(1,30001):
    nit = income*0.2
elif income in range(30000,80000):
    nit = (80000-income)*0.12
else:
    pass
if valid:
    print(f"Your negative income tax is {nit:.2f} Baht.")