def is_valid_number(number_str):
    if ',' in number_str:
        parts = number_str.split('.')
        integer_part = parts[0]
        
        if not all(integer_part[max(0, i-3):i].isdigit() for i in range(len(integer_part), 0, -4)):
            return False
        
        if len(parts) == 2 and len(parts[1]) != 2:
            return False

        if len(parts) == 2 and not parts[1].isdigit():
            return False
        
        return True
    else:
        parts = number_str.split('.')
        
        if len(parts) == 2 and len(parts[1]) != 2:
            return False
        
        if not parts[0].isdigit() or (len(parts) == 2 and not parts[1].isdigit()):
            return False
        
        return True

def clean_and_add_one(number_str):
    number_str = number_str.replace(',', '')
    
    if '.' in number_str:
        number = float(number_str)
        return f"{number + 1:.2f}"
    else:
        number = int(number_str)
        return str(number + 1)

input_str = input()

if is_valid_number(input_str):
    result = clean_and_add_one(input_str)
    print(result)
else:
    print("ERROR")