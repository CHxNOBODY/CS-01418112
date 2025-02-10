buffet = input("Enter your buffet choice: ")

if buffet == "Korean":
    day = input("Is today Wednesday (yes/no)? ")
    if day == "yes":
        print("Your payment is 1275.00 Baht.")
    else:
        print("Your payment is 1500.00 Baht.")

elif buffet == "Japanese":
    day = input("Is today Wednesday (yes/no)? ")
    if day == "yes":
        print("Your payment is 850.00 Baht.")
    else:
        print("Your payment is 1000.00 Baht.")
else:
    print(f"Sorry, there is no {buffet} buffet.")
    
