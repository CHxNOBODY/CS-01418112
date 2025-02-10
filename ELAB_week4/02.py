print("""---<< Main Menu >>---
    <B>urger Meal
    <C>hicken Meal
    <P>asta Meal""")

choice1 = input("Enter your choice: ")

if choice1 == "B" or choice1 == "b":
    print("""---<< Burger Sub Menu >>---
    <R>egular Burger
    <C>heese Burger
    <D>ouble Cheese Burger""")
    menu1 = input("Enter your choice: ")
    if menu1 == "R" or menu1 == "r":
        print("Your Regular Burger is 60 Baht.")
    elif menu1 == "C" or menu1 == "c":
        print("Your Cheese Burger is 75 Baht.")
    elif menu1 == "D" or menu1 == "d":
        print("Your Double Cheese Burger is 90 Baht.")
    elif menu1 != "R" or menu1 != "r" or menu1 != "C" or menu1 != "c" or menu1 != "D" or menu1 != "d":
        print("Invalid sub menu choice.")
elif choice1 == "C" or choice1 == "c":
    print("""---<< Chicken Sub Menu >>---
    <F>ried Chicken
    <G>rilled Chicken
    <C>hef's Chicken""")
    menu2 = input("Enter your choice: ")
    if menu2 == "F" or menu2 == "f":
        print("Your Fried Chicken is 120 Baht.")
    elif menu2 == "G" or menu2 == "g":
        print("Your Grilled Chicken is 150 Baht.")
    elif menu2 == "C" or menu2 == "c":
        print("Your Chef's Chicken is 180 Baht.")
    elif menu2 != "F" or menu2 != "f" or menu2 != "C" or menu2 != "c" or menu2 != "G" or menu2 != "g":
        print("Invalid sub menu choice.")
elif choice1 == "P" or choice1 =="p":
    print("""---<< Pasta Sub Menu >>---
    <S>paghetti de Italiano
    <L>asagna Supreme
    <M>acaroni Special""")
    menu3 = input("Enter your choice: ")
    if menu3 == "S" or menu3 == "s":
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif menu3 == "L" or menu3 == "l":
        print("Your Lasagna Supreme is 120 Baht.")
    elif menu3 == "M" or menu3 == "m":
        print("Your Macaroni Special is 100 Baht.")
    elif menu3 != "S" or menu3 != "s" or menu3 != "L" or menu3 != "l" or menu3 != "M" or menu3 != "m":
        print("Invalid sub menu choice.")
elif choice1 != "B" or choice1 != "b" or choice1 != "C" or choice1 != "c" or choice1 != "P" or choice1 != "p":
    print("Invalid main menu choice.")