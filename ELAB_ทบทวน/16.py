def reverse_string(s):
    n = len(s)
    mid = n // 2
    
    if n % 2 == 0:  # n is even
        first_half = s[:mid][::-1]
        second_half = s[mid:][::-1]
        result = first_half + second_half
    else:  # n is odd
        first_half = s[:mid][::-1]
        middle_char = s[mid]
        second_half = s[mid+1:][::-1]
        result = first_half + middle_char + second_half

    return result

input_string = input().strip()
output_string = reverse_string(input_string)
print(output_string)