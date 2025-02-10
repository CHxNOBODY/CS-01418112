def process_csv_line(s):
    parts = s.split(',')
    result = ''
    for part in parts:
        part = part.strip()  
        result += '"' + part + '"' + ','  
    return result[:-1]

s = input()
print(process_csv_line(s))