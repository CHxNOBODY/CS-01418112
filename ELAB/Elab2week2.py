print("First fraction:")
num1 = int(input(">>Enter a numerator a: "))
num2 = int(input(">>Enter a denominator b: "))

print("Second fraction:")
num3 = int(input(">>Enter a numerator c: "))
num4 = int(input(">>Enter a denominator d: "))

cal = (num1 * num4) + (num2 * num3)
cal2 = (num2 * num4)

print(f'Summation of the two fractions is {cal} / {cal2}')