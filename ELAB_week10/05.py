def filter_number():
    numbers = []
    while True:
        num = int(input())
        if num == -1:
            break
        numbers.append(num)
    
    new_numbers = [numbers[0]]
    for num in numbers[1:]:
        if num >= new_numbers[-1]:
            new_numbers.append(num)
    
    print(new_numbers)

filter_number()