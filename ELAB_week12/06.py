def validate_and_add_one_no_re(input_str):
    sanitized_input = input_str.replace(",", "")

    if sanitized_input.replace('.', '', 1).isdigit():
        if '.' in sanitized_input:
            decimal_part = sanitized_input.split('.')[1]
            if len(decimal_part) == 2: 
                num = float(sanitized_input)
                return f"{num + 1:.2f}"
            else:
                return "ERROR"
        else:
            num = int(sanitized_input)
            return str(num + 1)
    else:
        return "ERROR"

input_str = input()
print(validate_and_add_one_no_re(input_str))