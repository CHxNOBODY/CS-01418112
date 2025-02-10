def cut_str(s):
    cut = ''
    vowel = 'aeiouAEIOU'
    for i in s:
        if i not in vowel:
            cut += i
    return cut

s = input()
print(cut_str(s))