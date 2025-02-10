def extract_atom(chemical):
    atoms = {}
    st, num = '', ''
    st = chemical[0]
    
    for i in range(1, len(chemical)):
        ch = chemical[i]
        if ch.isalpha():
            if ch.isupper():
                if num == '':
                    num = '1'
                atoms[st] = num
                st, num = ch, ''
                continue
            else:
                st += ch
        else:
            num += ch    
    if num == '':
        num = 1
    atoms[st] = num
    
    return atoms

chemical = input()
atom = input()
atoms = extract_atom(chemical)
print(atoms.get(atom, 0))