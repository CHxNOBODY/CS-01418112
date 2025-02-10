def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        i = 1
        while i <= n:
           result *= i
           i += 1
        return result

number = int(input("Enter a number: "))

if number < 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i <= number:
        factors = ""
        j = i
        if i > 0:
            while j > 1:
                factors += f"{j} x "
                j -= 1
            factors += "1"
        else:
            factors = "1"
        print(f"{i}! = {factors} = {factorial(i)}")
        i += 1 

 