s = input()
count = 0

for i in range(len(s)):
    if 'a' in s[i] or 'A' in s[i]:
        count += 1
    if 'e' in s[i] or 'E' in s[i]:
        count += 1
    if 'i' in s[i] or 'I' in s[i]:
        count += 1
    if 'o' in s[i] or 'O' in s[i]:
        count += 1
    if 'u' in s[i] or 'U' in s[i]:
        count += 1
        
print(count)