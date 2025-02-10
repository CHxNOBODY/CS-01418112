def max_subarray_sum():
    numbers = []
    
    while True:
        num = int(input())
        if num == 0:
            break
        numbers.append(num)
    
    max_sum = float('-inf')
    current_sum = 0
    
    for number in numbers:
        current_sum += number
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    
    print(max_sum)

max_subarray_sum()