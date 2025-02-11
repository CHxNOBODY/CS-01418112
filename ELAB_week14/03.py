variables = {}
line = []

print('Enter variables and values:')
while True:
    text = input()
    if text == '-1':
        break
    [var, val] = text.split("=")
    var = var.strip()
    val = val.strip()
    variables[var] = val
    
print('Enter your program:')
while True: 
    text = input()
    if text == '-1':
        break
    for var in variables:
        key = '{' + var + '}'
        if key in text:
            text = text.replace(key, variables[var])
    line.append(text)
    
print('Result:')
for lines in line:
    print(lines)