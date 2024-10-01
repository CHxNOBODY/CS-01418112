def change(s):
    result = ""
    for i in s:
        if i == " ":
            result += "_"
        elif i in '\ / * : | " < >':
            result += "_"
        else:
            result += i
    if 