def get_hybrid_name(father, mother):
    def before_second_vowel(name):
        vowel_count = 0
        for i, char in enumerate(name):
            if char in 'aeiou':
                vowel_count += 1
                if vowel_count == 2:
                    return name[:i]
        return name

    def after_first_vowel(name):
        for i, char in enumerate(name):
            if char in 'aeiou':
                return name[i+1:]
        return name

    part_father = before_second_vowel(father)
    part_mother = after_first_vowel(mother)
    
    hybrid_name = part_father + part_mother
    return hybrid_name

father_name = input().strip()
mother_name = input().strip()

hybrid_name = get_hybrid_name(father_name, mother_name)

print(hybrid_name)