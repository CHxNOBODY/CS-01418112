def change(s):
    new = ''
    vowel = 'aeiou'
    for i in s:
        if i.lower() in vowel:
            new += i.upper()
        else:
            new += i.lower()
    return new

s = input()
print(change(s))