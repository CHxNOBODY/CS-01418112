tv1 = 6000
dvd1 = 1500
Audio = 3000

tv = float(input("How many TVs? "))
dvd = float(input("How many DVD players? "))
au = float(input("How many Audio Systems? "))
total = tv1*tv + dvd1*dvd + Audio*au

if total >= 24000:
    sum = total * 0.2
    print(f'Total price is {total:.2f} baht.')
    print(f"You've got a discount of {sum:.2f} baht.")
    print(f"Your payment is {total - sum:.2f} baht. Thank you!")
else:
    print(f'Total price is {total:.2f} baht.')
    print(f"Your payment is {total:.2f} baht. Thank you!")