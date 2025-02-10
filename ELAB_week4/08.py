due = int(input('Minutes before due: '))
temp = float(input('Temperature: '))
rain = input("Is it raining (y/n)? ").upper()

day = round(due/1440)
if day == 0:
    day = 1
print(f">>> {day} days before due.")
if day > 5:
    print(">>> I will not do the assignment.")
elif day < 2:
    print(">>> I will do the assignment.")
else:
    if temp > 40 or (temp > 25 and rain == "Y"):
        print(">>> I will not do the assignment.")
    else:
        print(">>> I will do the assignment.")