height = int(input("Enter height: "))
width = int(input("Enter width: "))

if height <= 0 or width <= 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i < height:
        j = 0
        while j < width:
            if i % 2 == 1:
                print(' *', end='')
            else:
                print('* ', end='')
            j += 1
        print()
        i += 1